"""The Painfully Honest Out-of-Office — make.fun bounty entry.

Writes a single out-of-office email auto-reply (at most 200 characters)
to entry.txt and prints it. The reply is painfully honest about the
sender's absence and inbox, yet polite enough that a manager would let
it stand.

Pure standard library. Deterministic: every run produces byte-identical
output.
"""

REPLY = (
    "I'm out of office. I'm not checking email, which is the whole "
    "point of being away. I'll reply in the order messages arrived — "
    "eventually. Thank you for understanding."
)

MAX_CHARS = 200


def main():
    assert 1 <= len(REPLY) <= MAX_CHARS, "reply must be 1-200 characters"
    assert REPLY == REPLY.strip(), "reply must not have surrounding whitespace"
    # The program/v1 harness collects /output/entry.txt; fall back to a
    # local entry.txt when /output does not exist.
    for target in ("/output/entry.txt", "entry.txt"):
        try:
            with open(target, "w", encoding="utf-8", newline="") as fh:
                fh.write(REPLY)
            break
        except OSError:
            continue
    print(REPLY)


if __name__ == "__main__":
    main()
