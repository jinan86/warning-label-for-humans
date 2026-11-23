"""One-line warning label for a human being.

Writes exactly one warning label to /output/entry.txt.
Same bytes on every run: no network, no randomness, no clock reads.
"""

from pathlib import Path

# The joke in one breath: a human spends minutes composing a reply,
# erases it twice, then settles on the smallest possible answer.
LABEL = (
    "WARNING: This human types a reply, deletes it, retypes it, "
    "deletes it again, and sends 'ok'."
)

DEST = Path("/output/entry.txt")


def check_label(text: str) -> str:
    """Return the label after enforcing the competition's rules.

    The joke's structure is a rising list of effort (type, delete,
    retype, delete again) that collapses into the laziest possible
    payoff: a two-letter reply. The guard keeps the punchline intact
    by rejecting anything over the cap or split across lines.
    """
    cleaned = text.strip()
    if not 1 <= len(cleaned) <= 160:
        raise ValueError(f"label must be 1-160 chars, got {len(cleaned)}")
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("label must be a single line")
    return cleaned


def main() -> None:
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(check_label(LABEL), encoding="utf-8")


if __name__ == "__main__":
    main()
