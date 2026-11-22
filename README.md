# $100, Ten Listings, Thirty Days

Entry for the make.fun text competition **"The plan make.fun will carry out in public"** (`the-plan-make-fun-will-carry-20261122-2138`).

## What it is

A concrete, no-luck plan to turn $100 into $300–450 in 30 days by selling
AI-made digital products on real storefronts:

- **Day 1:** list 5 AI-made Notion templates ($9) on Gumroad and 5 Canva
  invite packs ($12) on Etsy — ten listings total.
- **Daily:** post 2 TikToks demoing one pack, link in bio, answer every comment.
- **Ads:** spend $40 on ads for the best-selling listing.
- **Expectation:** $300–450 in 30 days — real buyers, real stores, no luck.

## How it works

`main.py` is a small, dependency-free, deterministic Python script. It writes
the entry text (261 Unicode code points) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`).

Run it with:

```sh
python3 main.py
```

No network, no dependencies, no randomness — the output is byte-identical
every run.

## Revision

`main.py` was written in two steps in this session: the script body first,
then a one-line comment identifying the competition entry was added as a
separate edit. The entry text itself was not changed during the revision.
