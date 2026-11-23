"""One-Line Laugh Sprint entry.

Writes a single original funny line about everyday life to
entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, or /output).
"""

import os

LINE = "I bought a standing desk so I'd sit less, then bought a chair for it."

MAX_CHARS = 200


def validate_entry(text: str) -> str:
    """Return the line if it passes the gate, else raise ValueError."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"entry must be 1-{MAX_CHARS} characters, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    text.encode("utf-8")  # must be encodable as UTF-8
    return text


def output_path() -> str:
    """Resolve the output file path, creating the directory if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def write_entry(text: str) -> str:
    """Validate the line and write it to the output file; return the path."""
    line = validate_entry(text)
    path = output_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(line)
    return path


def main() -> None:
    write_entry(LINE)


if __name__ == "__main__":
    main()
