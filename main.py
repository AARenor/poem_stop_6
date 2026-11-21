"""make.fun bounty the-poem-about-stopping-20261121-1927: write the poem to the output dir."""

import os
from pathlib import Path


def entry_path() -> Path:
    """The poem beside this file; a missing file raises FileNotFoundError."""
    return Path(__file__).resolve().parent / "entry.txt"


def output_path() -> Path:
    """Where the grader reads the poem: MAKEFUN_OUTPUT_DIR, /output by default."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> None:
    text = entry_path().read_bytes()
    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(text)


if __name__ == "__main__":
    main()
