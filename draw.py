#!/usr/bin/env python3
"""9カテゴリへISOコードを重複なしで割り当て、使うカテゴリ番号も乱数で決める。
結果はJSONで標準出力へ。reading.html の draw / selected にそのまま使う。"""
import json, os, random

CATS = ["国の文化", "海", "山", "ハイテク", "環境保全", "偉人", "虫", "動物", "植物"]
path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "iso_codes.txt")
iso = open(path).read().split()

rng = random.SystemRandom()  # OSの乱数（AIの意思が入らない）
draw = [{"n": i + 1, "cat": c, "iso": k} for i, (c, k) in enumerate(zip(CATS, rng.sample(iso, len(CATS))))]
print(json.dumps({"draw": draw, "selected": rng.randint(1, len(CATS))}, ensure_ascii=False, indent=1))
