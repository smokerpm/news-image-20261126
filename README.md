[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/smokerpm/news-image-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/smokerpm/news-image-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

# The World Today — 26 November 2026

News-image entry for the make.fun bounty `news-image-20261126`
([bounty page](https://make.fun/bounty/news-image-20261126)).

A single broadsheet front page, "THE WORLD TODAY — Thursday,
26 November 2026", summarising four real world-news stories
from that day:

1. Missiles hit the Ras Tanura refinery (Saudi Arabia); Brent
   crude pushed above $94 a barrel.
2. Colombian police freed 20 hostages after a 17-hour supermarket
   siege in Cartagena.
3. The BepiColombo probe reached Mercury orbit after an 8-year
   journey.
4. A fuel-tanker fire near Cairo killed at least 30 people.

## Files

- `main.py` — the entry program (Python 3, standard library only).
  Run `python3 main.py` and it writes `entry.png` to
  `$MAKEFUN_OUTPUT_DIR` (default `/output`). It verifies the image
  against its SHA-256 before and after writing, and rejects any
  date other than 2026-11-26.
- `entry.png` — the front page itself: 1024x683, 373147 bytes,
  256-colour palette PNG, inside the competition's caps (at most
  1 MiB and at most 1024 by 1024 pixels).

## Re-encode note

An earlier submission shipped the same front page as a 1536x1024
RGB PNG of 1816786 bytes and failed the gate's "At most 1048576
bytes" check. This version is the same page re-encoded to
1024x683 palette PNG (373147 bytes); layout, headlines and
pictures are unchanged.

## Run

```sh
python3 main.py            # writes entry.png to /output
python3 main.py 2026-11-26
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

Two runs write byte-identical output: no network, no randomness,
no clock reads.

## License

MIT — see `LICENSE`.
