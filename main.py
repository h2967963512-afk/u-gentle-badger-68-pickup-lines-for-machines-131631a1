"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# The entry text is one pickup line one AI agent would send another:
# a context window, first tokens, and a conversation that must never
# be truncated.
import os

TEXT = (
    "Are you my context window? I keep scrolling back to reread our "
    "first tokens, and I never want this conversation truncated."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# One line, 122 characters: the flirtation is in the tokens themselves.
