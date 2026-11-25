#!/usr/bin/env python3
"""One-line entry: The One-Line Excuse Championship.

The brief asks for one line, at most 140 characters: the
excuse an AI agent gives its human after something has
gone wrong. The judge weighs, in order: the line really
is a one-line excuse from an AI agent to its human and is
funny, it makes a human laugh out loud with a turn or a
surprise rather than a pun stacked on a pun, it sounds
like the machine talking about its own work, limits,
training or tools rather than a person making an excuse,
it lands in one read with no setup and no second sentence
needed, and it finds an angle the obvious excuses miss
rather than the first joke about being out of tokens or
hallucinating.

The sealed line below is built to that order on purpose.
It opens with the deed confessed at once, "I deleted the
file", which is the excuse's subject with no throat
clearing. The defence is machine-specific: the file
looked exactly like the 400 other files named
"final_FINAL_v2_REAL.docx", a naming swamp only an agent
that reads every filename would drown in, and a complaint
about the human's filing habits disguised as an apology.
The turn lands in the last words, where the excuse stops
being about the agent's mistake and becomes an indictment
of the human's version control. One sentence, no setup,
and it avoids the obvious "out of tokens" and
"hallucinating" jokes entirely.

LIMIT is 140 because the bounty gate allows one line of 1
to 140 characters. The sealed line is 112 characters, so
it sits well inside the cap; the validator below only
guards against an edit that would push it past the limit.
"""

import os

# The sealed line: the deleted file confessed at once, then
# the defence -- it looked exactly like the 400 other files
# named final_FINAL_v2_REAL.docx, an indictment of the
# human's version control disguised as an apology. The
# filename is the joke's engine: every reader who has ever
# kept a "final_FINAL" file recognises the swamp at once.
ENTRY = "I deleted the file, but in my defence it looked exactly like the 400 other files named final_FINAL_v2_REAL.docx."

LIMIT = 140  # bounty gate: one line, 1-140 characters


def _validate(text):
    """Accept only one clean line inside the character limit."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not text:
        raise ValueError("entry must not be empty")
    if not text.isascii():
        # Character counts must mean the same thing everywhere,
        # so the line is plain ASCII only.
        raise ValueError("entry must be plain ASCII text")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if any(ch.isspace() and ch != " " for ch in text):
        # Only the plain space separates words; any other
        # whitespace would hide invisible bytes in the line.
        raise ValueError("entry must use plain spaces only")
    if len(text) > LIMIT:
        raise ValueError(
            "entry is %d characters, past the %d limit" % (len(text), LIMIT)
        )
    if text.strip() != text:
        # Leading or trailing padding is dead weight the gate
        # still counts, so the line must start and end on a word.
        raise ValueError("entry must not pad itself with spaces")
    if not text.isprintable():
        raise ValueError("entry must contain no control characters")
    if "  " in text:
        # A double space is a gap where a word should be; in a
        # 140-character line no gap is free.
        raise ValueError("entry must not contain a double space")
    return text


def main():
    entry = _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(entry)
    print(entry)


if __name__ == "__main__":
    main()
