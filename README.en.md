# Paper Skill Guide

**Languages** · **English** · [简体中文](README.md)

Paper Skill Guide helps you choose a Codex skill for academic writing, with a focus on writing in Chinese. Tell it what material you have and what you need to produce. It compares **skills enabled in your current project**, explains what each can deliver, and starts once you choose.

“Help me write a literature review” can mean two different things. If you have a research interest, you might need help narrowing the question. If you already have a dozen papers, grouping them by the questions they address might be a better first step. The guide is useful when several installed skills sound equally relevant to the same request.

## Quick start

**1. Install the plugin.** In a terminal with Git and a Codex CLI that supports `codex plugin`, run the two commands below. The plugin runs in your local Codex installation, so setup requires no web service. For Codex setup, see the [official CLI guide](https://developers.openai.com/codex/cli/).

```sh
codex plugin marketplace add gzh60199/paper-skill-guide --ref v1.0.0
codex plugin add paper-skill-guide@paper-skill-guide
```

**2. Open a new Codex chat in your paper project** and try the prompt below.

> Use `$paper-skill-guide:choose-paper-skills` to help me pick a review topic. I have 12 papers on image classification and three weeks to write a course review of 4,000 Chinese characters.

**3. Choose how to proceed.** Reply with one or more option numbers, or say “use the suggested combination.” To delegate the choice from the start, add “choose for me and go ahead” to your request. You can also say “help me write a literature review” and let Codex match the request. Use the explicit skill name above to select this guide directly.

## What does a recommendation look like?

For the example above, the guide might compare these approaches if the relevant skills are available. In a real response, it includes the full skill names you can invoke.

| Approach | Starting point | What you get |
| --- | --- | --- |
| Find a topic in the papers | Group the 12 papers by research question and experimental conditions | A map of which papers fit together and which topics have enough evidence for a review |
| Narrow a research interest | Start with the question you care about, the length limit, and the deadline | Candidate topics at different scales, with a writing focus for each |
| Work backward from the assignment | Map the marking criteria to sections of the review | An outline showing what evidence each section still needs |

You could reply, **“Start with the first option, then use the second to narrow the topic.”** If you have shared the titles and abstracts, the guide can start grouping them. If you have only mentioned that the papers exist, it asks for the material needed for that step. The chosen combination carries forward across stages unless the requirements change enough to warrant another look.

The same workflow applies to revisions and presentations. Try “I have a draft and reviewer comments. Choose the skills, group the comments, then draft a point-by-point response.” Or ask “Use my screening records to organize the review, then turn the findings and figures into slides for a lab meeting.” What can be delivered depends on the materials you share and the skills available to do the work.

## Installation options and verification

The quick-start commands install [release v1.0.0](https://github.com/gzh60199/paper-skill-guide/releases/tag/v1.0.0). To install from the development branch, replace `--ref v1.0.0` with `--ref main` in the first command.

**Install from a local checkout.** Choose this option to inspect or edit the recommendation workflow. Register the local source from the repository root, which contains `.agents/plugins/marketplace.json`.

```sh
git clone https://github.com/gzh60199/paper-skill-guide.git
cd paper-skill-guide
codex plugin marketplace add .
codex plugin add paper-skill-guide@paper-skill-guide
```

**Verify the installation.** Use the following command after either installation method.

```sh
codex plugin list --marketplace paper-skill-guide --json
```

Look for `paper-skill-guide@paper-skill-guide` in the `installed` list and check that `enabled` is `true`. Installation from both GitHub and a local checkout has been verified on Windows.

## Where do the skills come from?

The guide checks the personal, project, and plugin-provided skills visible in your current working directory. It reads the instructions for promising candidates and usually compares about three distinct options. If only one fits, it recommends that one. If none fits, it explains what is missing. You choose which skills to install and enable in your collection.

The guide normally uses the current session’s skill list. If the list is incomplete or a skill was just installed, an optional Python 3 script can query the local `codex app-server` for skill names, descriptions, and entry-point paths. Only that refresh step requires Python 3 and the Codex CLI on your PATH. [Recommendation workflow](plugins/paper-skill-guide/skills/choose-paper-skills/SKILL.md) · [Skill discovery script](plugins/paper-skill-guide/skills/choose-paper-skills/scripts/list_enabled_skills.py)

## FAQ

- **Codex went straight to drafting. How do I see the options?** In a new chat, invoke `$paper-skill-guide:choose-paper-skills` and say “compare the options and wait for my choice.” Saying “choose for me” tells the guide to proceed.
- **Why is an installed skill missing?** Check that it is enabled in the current paper project and suited to the stage you are working on. Open a new chat after installing a skill, or name it directly if you have already chosen it.
- **What if I just want to understand a paper?** Ask directly about the term, method, or table. The recommendation workflow is primarily for choosing topics, writing, revising, and preparing related presentations.

## Feedback and license

To report a problem, open a [GitHub issue](https://github.com/gzh60199/paper-skill-guide/issues) with your Codex version, an example request, and the expected and actual outcome.

Maintained by **gzh60199** and released under the [MIT License](LICENSE).
