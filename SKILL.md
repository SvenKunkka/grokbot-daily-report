---
name: daily-report-draft
description: 需要根据当天聊天、任务和交付整理工作日报时使用；只生成草稿供本人审核，绝不自动发送。
---
# 步骤
1. 用 lark-cli（只读）或其他来源导出当天消息、任务、日程为 NDJSON。
2. `scripts/collect_day.py events.ndjson --date YYYY-MM-DD` 生成素材。
3. 按「今日完成 / 进行中 / 风险与阻塞 / 明日计划」写草稿，每条附证据（会话或文档）。
4. 非主业内容单独列出，仅供本人查看。
5. 把草稿交给本人审核；发送与否由本人决定。
