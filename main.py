#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one dad joke to /output/entry.txt. The joke is a fixed, deterministic
string: no randomness, no network, no input, so every run produces the exact
same bytes.
"""

import os

JOKE = (
    "I told my wife I got hired as a human cannonball. "
    "She said, 'Just don't get fired.'"
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
