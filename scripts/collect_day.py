#!/usr/bin/env python3
"""按日期收集事件并按会话分组，输出日报素材（不发送任何内容）。"""
import argparse, json, sys
from collections import defaultdict
from datetime import datetime, timezone, timedelta

def ts(v, tz):
    if isinstance(v, (int, float)) or (isinstance(v, str) and v.isdigit()):
        v = int(v); v = v / 1000 if v > 1e12 else v
        return datetime.fromtimestamp(v, tz)
    return datetime.fromisoformat(str(v).replace("Z", "+00:00")).astimezone(tz)

def load(path):
    raw = open(path, encoding="utf-8").read().strip()
    if raw.startswith("["): return json.loads(raw)
    return [json.loads(l) for l in raw.splitlines() if l.strip()]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument("file"); ap.add_argument("--date", required=True)
    ap.add_argument("--utc-offset", type=float, default=8.0)
    a = ap.parse_args(); tz = timezone(timedelta(hours=a.utc_offset))
    groups = defaultdict(list)
    for e in load(a.file):
        t = e.get("time") or e.get("create_time") or e.get("timestamp")
        if t is None: continue
        d = ts(t, tz)
        if d.strftime("%Y-%m-%d") != a.date: continue
        groups[e.get("chat") or e.get("chat_name") or "未知会话"].append((d, e.get("sender", ""), (e.get("text") or e.get("content") or "").strip()))
    print(f"# {a.date} 日报素材（{sum(map(len, groups.values()))} 条）\n")
    for chat, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        print(f"## {chat}（{len(items)} 条）")
        for d, s, t in sorted(items): print(f"- {d:%H:%M} {s}: {t[:200]}")
        print()

if __name__ == "__main__":
    sys.exit(main())
