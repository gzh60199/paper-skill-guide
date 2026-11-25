# Paper Skill Guide

**Languages** · **English** · [简体中文](README.md)

Paper Skill Guide helps you choose among the **Codex skills available in your current project** when writing a paper, narrowing a literature review topic, or responding to reviewers. Pick a skill, accept a suggested combination, or ask Codex to choose and get started.

## Installation

Run these commands in a terminal where `codex plugin` is available:

```sh
codex plugin marketplace add gzh60199/paper-skill-guide --ref main
codex plugin add paper-skill-guide@paper-skill-guide
```

Start a new Codex chat and try one of the examples below. Codex can match a request to the guide automatically. To invoke it explicitly, mention `$paper-skill-guide:choose-paper-skills`. To check the installation, run `codex plugin list --marketplace paper-skill-guide`.

## Examples

> I have 12 papers on image classification and three weeks to write a course literature review of 4,000 Chinese characters. Help me settle on a topic first.

If you have skills for reviewing literature, choosing a topic, and planning a paper, the guide can compare three approaches: find a question that several of your papers address, narrow the scope around your interests, or work backward from the course requirements to outline the review. For each option, it gives the installed skill’s name, the materials it needs, what it can produce, and the trade-offs. Reply with an option number or combine steps: “Group the papers first, then help me narrow the topic. Go ahead with that combination.”

> I have my screening records and a first draft. Choose the skills for me. First, organize the reviewers’ comments about gaps in the literature coverage, then draft a response.

When you delegate the choice, the guide briefly explains its reasoning and starts the work it can do with the available materials. If you name a skill, it follows your choice. If you simply ask what a term in a paper means, you get a direct explanation.

## Skill discovery and compatibility

- The guide usually compares about three distinct options. If only one fits, it recommends that one. If none fits the current stage, it explains what is missing and suggests a workable next step.
- Candidates come from enabled personal, project, and plugin skills. You can use your existing skill collection. The guide does not automatically install candidates.
- The guide uses the current session’s skill list by default. To refresh it, an optional Python 3 script queries the local `codex app-server` for skill names, descriptions, and entry-point paths in the current project. Running the script requires Python 3 and the Codex CLI on your PATH.
- The plugin is designed primarily for writing in Chinese. Installation has been verified on Windows. The papers, drafts, figures, or slides a workflow can deliver depend on the available skills and tools, and on the materials you provide.

## License

Maintained by **gzh60199** and released under the [MIT License](LICENSE).
