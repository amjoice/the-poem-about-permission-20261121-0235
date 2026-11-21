#!/usr/bin/env python3
"""Permission — a single original poem, written to /output/entry.txt.

Pure standard library. Deterministic: every run writes identical bytes.
No network, no randomness, no input files.
"""

import os

POEM = """Permission

I asked the door if I might enter,
and the door said nothing at all.
No lock, no key, no stern dissenter —
only the echo down the hall.

I waited for a voice to grant me
passage, pardon, place, or plan,
a stamp, a seal, a hand to hand me
leave to be the one I am.

But permission was not in the asking,
nor in the silence after the knock.
It was the step I kept on taking,
the turning of my own lock.

The door was never closed against me.
It only waited, patient, true,
for me to learn the key was simply
the courage to walk through.
"""

OUTPUT_PATH = os.environ.get("POEM_OUTPUT_PATH", "/output/entry.txt")


def main():
    text = POEM
    if not text.endswith("\n"):
        text += "\n"
    if not (1 <= len(text) <= 1000):
        raise SystemExit("poem must be 1-1000 characters, got %d" % len(text))
    directory = os.path.dirname(OUTPUT_PATH)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
