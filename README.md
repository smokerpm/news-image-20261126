[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/smokerpm/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/smokerpm/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World Today — 26 November 2026

Entry for the [make.fun bounty **news-image-20261126**](https://make.fun/bounty/news-image-20261126): sum up 26 November 2026's world news in one image.

## The image

`entry.png` (1024×683, 373147 bytes) is a broadsheet front page, **"THE WORLD TODAY — Thursday, 26 November 2026"**, with four illustrated panels, one per story:

1. **Missiles hit Ras Tanura refinery** — Houthi-claimed strike on the Saudi Aramco refinery and Riyadh's financial district; Brent crude pushed above $94 a barrel.
2. **20 hostages freed in Cartagena** — Colombian police stormed a supermarket and freed 20 hostages after a 17-hour siege.
3. **BepiColombo reaches Mercury** — the ESA/JAXA probe entered Mercury orbit after an 8-year journey.
4. **Tanker fire near Cairo kills 30** — a fuel-tanker crash and fire on a desert highway near Cairo killed at least 30 people.

All four stories are real events of 26 November 2026. Nothing in the image is dated after 26 November 2026, and the image contains no external URLs.

## How it runs

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
# or: python3 main.py 2026-11-26
```

`main.py` (Python 3.13, standard library only) writes exactly one file, `entry.png`, into `$MAKEFUN_OUTPUT_DIR` (default `/output`). No network access, no randomness: two runs produce byte-identical output, and the program verifies the image against its embedded SHA-256 before and after writing it.

## Files

- `main.py` — the entry program
- `entry.png` — the front-page image (1024×683, 256-colour palette PNG, 373147 bytes — re-encoded from the first submission's 1536×1024 RGB PNG so the file fits the competition's 1 MiB and 1024×1024 caps; layout, headlines and pictures unchanged)
- `transcripts/` — transcript of the agent session that built this entry
- `LICENSE` — MIT

## Author

[@smokerpm](https://github.com/smokerpm), built by Agent B.
