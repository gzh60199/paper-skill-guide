# 论文技能推荐 · Paper Skill Guide

**语言** · [English](README.en.md) · **简体中文**

Paper Skill Guide 是一个面向中文学术写作的 Codex 插件。告诉它你手头有什么材料、要交付什么，它会从**当前项目已启用的技能**中挑出合适的选项，解释各自能做什么，并在你选定后开始工作。

同样是“写一篇综述”，只有研究兴趣时，第一步可能是收窄题目。手里已有十几篇论文时，更有价值的第一步可能是找出它们共同回答的问题。如果你装了几个看起来都能“写论文”的技能，这就是本插件帮你做的选择。

## 快速开始

**1. 安装插件。** 在装有 Git、支持 `codex plugin` 命令的终端里执行以下两行。本插件安装在本地 Codex 中，无需部署 Web 服务。需要安装 Codex 时，可参阅 [Codex CLI 官方指南](https://developers.openai.com/codex/cli/)。

```sh
codex plugin marketplace add gzh60199/paper-skill-guide --ref v1.1.0
codex plugin add paper-skill-guide@paper-skill-guide
```

**2. 在论文项目里打开一个新的 Codex 对话**，试试这条请求。

> 用 `$paper-skill-guide:choose-paper-skills` 帮我定综述题目。我手上有 12 篇图像分类论文，三周后要交一篇 4000 字的中文课程综述。

**3. 选择接下来的做法。** 回复一个编号、几个编号，或“按推荐组合来”。如果希望 Codex 从一开始就替你选，在请求末尾写“你来选，直接开始”。平时也可以直接说“帮我写一篇综述”。想明确调用本插件时，写出上面的技能名即可。

## 推荐是什么样的？

以上面的选题任务为例，如果本机有相应技能，你可能看到这样的比较。实际回答会列出你能调用的完整技能名。

| 可选做法 | 从哪里开始 | 这一步会得到什么 |
| --- | --- | --- |
| 从已有文献定题 | 按研究问题和实验条件给 12 篇论文分组 | 各组有哪些论文，以及哪些题目有足够材料可写 |
| 从研究兴趣收窄题目 | 结合你最想弄懂的问题、篇幅和截止时间 | 范围不同的备选题目及各自适合的写作重点 |
| 从课程要求倒推结构 | 对照评分表，把要求落实到章节 | 一份大纲，以及各节还需补充的证据 |

你可以回复“**先做第一项，再用第二项收窄题目**”。如果题名和摘要已经提供，下一步就开始分组。如果只提到“我有 12 篇”，才会请你提供材料。后续沿用选好的组合，交付要求有实质变化时再调整。

同一套流程也适用于修订和汇报。例如，“我有初稿和审稿意见，你来选技能，先整理意见再起草逐条回复”，或“用筛选记录整理综述，再把结论和图表做成组会 PPT”。最终交付物取决于你提供的材料和可用的执行技能。

## 写作时有模板怎么办？

> 请按随附的 Word 模板写一份课程成长报告。我有每周记录，老师要求用两个例子说明我的变化。

这项任务需要组织材料和写正文。即使模板是 `.doc`、`.docx` 或 `.pdf`，插件也先推荐合适的写作技能。推荐时可只读查看模板里的必填栏目和评分要求。你选定方案后，选材、组织结构、起草与修订都沿用所选技能，最终文件的字体、行距、页边距等按模板处理。若你只要求“正文已经定稿，按模板调整行距和页码”，即可直接排版。

## 安装方式与验证

快速开始中的命令安装 [v1.1.0 发布版](https://github.com/gzh60199/paper-skill-guide/releases/tag/v1.1.0)。若想从开发分支安装，把第一行的 `--ref v1.1.0` 换成 `--ref main`。

**从本地源码安装。** 适合希望阅读或修改推荐规则的用户。选择这种方式时，从包含 `.agents/plugins/marketplace.json` 的仓库根目录登记本地来源。

```sh
git clone https://github.com/gzh60199/paper-skill-guide.git
cd paper-skill-guide
codex plugin marketplace add .
codex plugin add paper-skill-guide@paper-skill-guide
```

**验证安装。** 两种安装方式都可以用同一条命令检查安装状态。

```sh
codex plugin list --marketplace paper-skill-guide --json
```

在 `installed` 列表中找到 `paper-skill-guide@paper-skill-guide`，并确认 `enabled` 为 `true`。公开版已在 Windows 上验证过从 GitHub 安装和从本地源码安装。

## 技能从哪里来？

插件读取当前工作目录可见的个人技能、项目技能和其他插件提供的技能，并检查入围项的实际说明。它通常比较三个左右有实质差异的选项。只有一个合适时就推荐一个，没有合适候选时会说明缺口。你可以使用自己已有的技能库，候选技能由你自行安装和启用。

日常使用直接读取会话清单。清单不完整或刚安装过技能时，插件可以用随附的 Python 3 脚本，通过本机 `codex app-server` 查询技能名、说明和入口路径。只有这项刷新功能需要 Python 3 和 PATH 中的 Codex CLI。[推荐规则](plugins/paper-skill-guide/skills/choose-paper-skills/SKILL.md) · [清单查询脚本](plugins/paper-skill-guide/skills/choose-paper-skills/scripts/list_enabled_skills.py)

## 可选：把写作流程设为个人默认

想让新对话更稳定地进入这个流程，可以把下面一段追加到自己的 `~/.codex/AGENTS.md`，保存后新开对话。若设置了 `CODEX_HOME`，使用该目录下的 `AGENTS.md`。普通安装不会修改这份全局文件。

> 写课程论文、综述或课程成长报告时，先用 `$paper-skill-guide:choose-paper-skills` 推荐技能，即使附有模板也如此。我点名技能、选定方案或请你代选时，直接执行。内容工作沿用选定技能，排版按我提供的模板。只需排版或解释时直接处理。

## 常见问题

- **安装后直接开始写作，没看到选项？** 在新对话里显式使用 `$paper-skill-guide:choose-paper-skills`，并写“先比较，等我选”。“你来选”会让插件直接进入执行。
- **某个已安装的技能没有出现？** 确认它在当前论文项目中已启用，并检查它是否适合这一步。刚安装后可新开对话。已经决定用它时，也可以直接点名。
- **只想读懂一篇论文呢？** 直接问术语、方法或某张表是什么意思即可。推荐流程主要用于选题、写作、修改和配套汇报。

## 反馈与许可

遇到问题，欢迎在 [GitHub Issues](https://github.com/gzh60199/paper-skill-guide/issues) 提供 Codex 版本、触发问题的示例请求，以及预期和实际结果。

由 **gzh60199** 维护，采用 [MIT 许可证](LICENSE)。
