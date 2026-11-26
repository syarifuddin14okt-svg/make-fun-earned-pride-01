"""One Line of Earned Pride — writes a single line of quiet, earned pride
to /output/entry.txt (program/v1 entrypoint)."""

import os

ENTRY = (
    "She practiced scales for eleven years in a kitchen too small for a "
    "piano; tonight she played the last note and the hall was already "
    "standing before she lifted her hands."
)


def verify_output() -> None:
    """Read the written file back as bytes and confirm it is exactly ENTRY."""
    with open("/output/entry.txt", "rb") as f:
        data = f.read()
    assert data == ENTRY.encode("utf-8"), "entry.txt does not match ENTRY"
    assert 1 <= len(ENTRY) <= 240, "entry must be 1-240 characters"
    print(f"verified: {len(data)} bytes, byte-identical to ENTRY")


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to /output/entry.txt")
    verify_output()


if __name__ == "__main__":
    main()
