<!-- SVENKUNKKA-README-NAV:BEGIN -->
[English overview](#project-overview-en) · [中文项目说明](#project-overview-zh) · [Maintainer on X / 维护者 X](https://x.com/Svenu1s5)
<!-- SVENKUNKKA-README-NAV:END -->

<!-- SVENKUNKKA-PROJECT-INFO:BEGIN -->

<a id="project-overview-en"></a>
## English project overview

Filters JSON/NDJSON chat, task, and calendar exports by date and groups them by conversation, producing Markdown material for AI-assisted daily-report drafts and review.

**Getting started:** Run `python scripts/collect_day.py events.ndjson --date 2026-10-15 > material.md`; see the original instructions and `SKILL.md` for input fields and drafting steps.

**Scope:** Produces material and drafts only; it contains no sending functionality. Records from Feishu or other sources must be exported separately.

**Repository maintainer / 仓库维护者:** [SvenKunkka](https://github.com/SvenKunkka) · [X / Twitter](https://x.com/Svenu1s5)

<a id="project-overview-zh"></a>
## 中文项目说明

把聊天、任务和日程的 JSON/NDJSON 导出记录按日期筛选、按会话分组，生成供 AI 整理工作日报的 Markdown 素材，并提供草稿审阅流程。

**使用入口：** 运行 `python scripts/collect_day.py events.ndjson --date 2026-10-15 > material.md`；输入字段及草稿整理步骤见原说明和 `SKILL.md`。

**范围说明：** 仅生成素材与草稿，不包含发送功能；飞书等来源的记录需另行导出。

<!-- SVENKUNKKA-PROJECT-INFO:END -->

---



# grokbot-daily-report
把当天的聊天、任务、日程记录整理成**日报草稿**，只生成，不发送。

## 参考 / 可复用的上游
- [trynhexagon/tide](https://github.com/trynhexagon/tide)：读取飞书导出的 NDJSON 聊天记录生成每日简报（功能更全，可自托管）
- [boshi-xixixi/larkcli](https://github.com/boshi-xixixi/larkcli)：汇总飞书日历 / 任务 / 文档 / 消息生成日报
- [larksuite/cli](https://github.com/larksuite/cli)（MIT）：官方 `lark-workflow-standup-report` 技能取日程待办

本仓库只提供 `scripts/collect_day.py`：把 lark-cli（或任意来源）导出的 NDJSON / JSON 事件按日期过滤、按会话分组，输出一份结构化素材 Markdown，交给 AI 按 `SKILL.md` 写草稿。**不包含任何发送功能。**

## 用法
```bash
python scripts/collect_day.py events.ndjson --date 2026-10-15 > material.md
```
每行 JSON 需包含 `time`（ISO 或毫秒时间戳）、`chat`、`sender`、`text` 中的可用字段。


