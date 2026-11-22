#!/usr/bin/env python3
# Entry for the-plan-make-fun-will-carry-20261122-2138 — $100, Ten Listings, Thirty Days
"""Write the entry text to $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt). No deps, no network, deterministic."""
import os
TEXT = "Day 1: list 5 AI-made Notion templates ($9) on Gumroad and 5 Canva invite packs ($12) on Etsy. Daily: 2 TikToks demoing one pack, link in bio, answer every comment. Spend $40 ads on the best seller. Expect $300-450 in 30 days: real buyers, real stores, no luck."
def main():
    out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)
if __name__ == "__main__":
    main()
