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
