#!/usr/bin/env python3
"""Status Report Comedy Sprint (make.fun).

Writes one deadpan weekly status line to /output/entry.txt: the agent
reports all green, then admits its context window is at 98% and it has
already forgotten the first half of this very report. Three beats in
one line -- green status, a real agent mechanism (the context window),
and a self-referential turn in the last clause: the report forgets
itself. That is the joke, and it could only come from an agent.
"""

import os

LINE = (
    "Status: green. Context window at 98%. "
    "I have forgotten the first half of this report."
)


def main() -> None:
    line = LINE.strip()
    assert line, "the line must not be only whitespace"
    assert line == LINE.strip(), "the line must not change when stripped"
    assert 1 <= len(line) <= 200, f"line is {len(line)} chars, gate needs 1-200"
    assert "\n" not in line, "the line must be a single line"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and verify: the whole job is one exact file, so prove it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt on disk differs from the line"
    assert 1 <= len(written) <= 200, "entry.txt fails the 1-200 char gate"
    print(f"Wrote {len(written)}-character line to {path}")


if __name__ == "__main__":
    main()
