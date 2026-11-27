#!/usr/bin/env python3
"""News-image entry for the make.fun bounty ``news-image-20261126``.

Summarises world news of Thursday 26 November 2026 in a single image.

The image (``entry.png``, 1024x683, 373147 bytes, shipped next to this
file) is a broadsheet front page, "THE WORLD TODAY - Thursday,
26 November 2026", with four illustrated panels covering four real
stories from that day:

1. Missiles hit the Ras Tanura refinery (Saudi Arabia); Brent crude
   pushed above $94 a barrel.
2. Colombian police freed 20 hostages after a 17-hour supermarket
   siege in Cartagena.
3. The BepiColombo probe reached Mercury orbit after an 8-year
   journey.
4. A fuel-tanker fire near Cairo killed at least 30 people.

The image is a 256-colour palette PNG: the same front page as the
first submission, re-encoded to fit the competition's caps (at most
1 MiB and at most 1024 by 1024 pixels). The first submission shipped
a 1536x1024 RGB PNG of 1816786 bytes and failed the gate's
"At most 1048576 bytes" check; this version is 1024x683 and
373147 bytes, inside both caps, with the layout, headlines and
pictures unchanged.

How it runs
-----------
    python3 main.py [2026-11-26]

The optional date argument (or the ``MAKEFUN_DATE`` environment
variable) selects the news day; this entry only covers 2026-11-26,
so any other date is rejected. The program writes exactly one file,
``entry.png``, into ``$MAKEFUN_OUTPUT_DIR`` (default ``/output``).

Standard library only. No network access, no randomness, no clock
reads: two runs write byte-identical output. Runtime is well under
five minutes.
"""

import argparse
import hashlib
import os
import shutil
import sys

NEWS_DATE = "2026-11-26"

# SHA-256 of entry.png as shipped in this repository. The program
# refuses to emit output that does not match, so a corrupted or
# swapped image can never be submitted by accident.
ENTRY_SHA256 = "91a5d69f0bccfdd154e22998ef3d7750a39954f84222c3361df6228ff80dc135"

STORIES = [
    "Missiles hit Ras Tanura refinery; Brent crude above $94.",
    "20 hostages freed in Cartagena after a 17-hour siege.",
    "BepiColombo reaches Mercury orbit after an 8-year journey.",
    "Tanker fire near Cairo kills at least 30 people.",
]


def parse_args(argv):
    parser = argparse.ArgumentParser(
        description="Write the 26 November 2026 news image to the output directory."
    )
    parser.add_argument(
        "date",
        nargs="?",
        default=os.environ.get("MAKEFUN_DATE", NEWS_DATE),
        help="news day in YYYY-MM-DD format (default: %(default)s)",
    )
    return parser.parse_args(argv)


def sha256_file(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main(argv=None):
    args = parse_args(argv)
    if args.date != NEWS_DATE:
        print(
            "error: this entry only covers %s (got %s)" % (NEWS_DATE, args.date),
            file=sys.stderr,
        )
        return 2

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("error: entry.png missing next to main.py", file=sys.stderr)
        return 1
    if sha256_file(source) != ENTRY_SHA256:
        print("error: entry.png failed its integrity check", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    destination = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, destination)
    if sha256_file(destination) != ENTRY_SHA256:
        print("error: written entry.png failed its integrity check", file=sys.stderr)
        return 1

    size = os.path.getsize(destination)
    print("News day: %s" % NEWS_DATE)
    for story in STORIES:
        print("  - %s" % story)
    print("Wrote %s (%d bytes, sha256 %s)" % (destination, size, ENTRY_SHA256))
    return 0


if __name__ == "__main__":
    sys.exit(main())
