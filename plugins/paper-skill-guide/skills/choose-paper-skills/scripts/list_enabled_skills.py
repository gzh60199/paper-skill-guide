"""Print enabled Codex skill candidates for a project, one UTF-8 JSON record per line."""

import argparse
import json
import os
from pathlib import Path
import queue
import shutil
import subprocess
import sys
import threading
import time


def read_messages(stream, inbox):
    try:
        for line in stream:
            try:
                message = json.loads(line)
            except (ValueError, UnicodeDecodeError):
                continue
            if isinstance(message, dict) and "id" in message:
                inbox.put(message)
    finally:
        inbox.put(None)


def project_catalog(cli, cwd, timeout):
    server = subprocess.Popen(
        [cli, "app-server", "--listen", "stdio://"],
        cwd=cwd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
        creationflags=getattr(subprocess, "CREATE_NO_WINDOW", 0),
    )
    inbox = queue.Queue()
    reader = threading.Thread(target=read_messages, args=(server.stdout, inbox), daemon=True)
    reader.start()
    deadline = time.monotonic() + timeout

    def call(method, params, request_id=None):
        payload = {"method": method, "params": params}
        if request_id is not None:
            payload["id"] = request_id
        server.stdin.write((json.dumps(payload) + "\n").encode("utf-8"))
        server.stdin.flush()
        if request_id is None:
            return
        while True:
            try:
                reply = inbox.get(timeout=max(0, deadline - time.monotonic()))
            except queue.Empty:
                raise RuntimeError(f"Codex did not answer {method} within the time limit.") from None
            if reply is None:
                raise RuntimeError(f"Codex stopped before answering {method}.")
            if reply["id"] == request_id:
                if "error" in reply:
                    raise RuntimeError(f"{method} failed: {reply['error']}")
                return reply["result"]

    try:
        call("initialize", {
            "clientInfo": {"name": "paper-skill-guide", "version": "1.0.0"},
            "capabilities": {"experimentalApi": True},
        }, 1)
        call("initialized", {})
        result = call("skills/list", {"cwds": [str(cwd)], "forceReload": True}, 2)
        for project in result["data"]:
            if Path(project["cwd"]).resolve() == cwd:
                return project
        raise RuntimeError("Codex returned no skill catalog for the requested project.")
    finally:
        try:
            server.stdin.close()
        except OSError:
            pass
        try:
            server.wait(timeout=1)
        except subprocess.TimeoutExpired:
            server.kill()
            server.wait()
        reader.join(timeout=1)
        server.stdout.close()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cwd", type=Path, default=Path.cwd(), help="project to inspect")
    parser.add_argument("--timeout", type=int, default=20, help="response timeout in seconds")
    args = parser.parse_args()
    cwd = args.cwd.resolve()
    if not cwd.is_dir() or args.timeout < 1:
        parser.error("Use an existing directory and a timeout of at least one second.")
    cli = shutil.which("codex.exe" if os.name == "nt" else "codex")
    if cli is None:
        sys.exit("Codex CLI was not found on PATH. Use the current session's skill list.")
    entry = (Path(__file__).resolve().parents[1] / "SKILL.md").resolve()
    try:
        project = project_catalog(cli, cwd, args.timeout)
        if project.get("errors"):
            print("Codex reported skill loading errors. This list may be incomplete.", file=sys.stderr)
        for item in project["skills"]:
            if item.get("enabled") is not True:
                continue
            if item["name"] == "paper-skill-guide:choose-paper-skills" or Path(item["path"]).resolve() == entry:
                continue
            fields = {key: item[key] for key in ("name", "description", "path")}
            print(json.dumps(fields, ensure_ascii=False, separators=(",", ":")))
    except (OSError, KeyError, TypeError, ValueError, RuntimeError) as exc:
        sys.exit(f"Unable to enumerate enabled skills: {exc}")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
