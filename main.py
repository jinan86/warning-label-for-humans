"""Warning Label for Humans: One Line, Big Laugh.

Writes one single-line safety warning label for human beings to
/output/entry.txt. Deterministic: every run writes the exact same bytes.
No network, no randomness, no input files.
"""

from pathlib import Path

# One idea, one line: the human who labours over a reply, then sends "ok".
# Turn lands in the last words; 92 characters, inside the 160 cap.
LABEL = (
    "WARNING: This human types a reply, deletes it, retypes it, "
    "deletes it again, and sends 'ok'."
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    text = LABEL.strip()
    assert 1 <= len(text) <= 160, f"label must be 1-160 chars, got {len(text)}"
    assert "\n" not in text, "label must be a single line"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
