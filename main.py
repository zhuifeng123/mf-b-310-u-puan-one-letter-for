from pathlib import Path

ENTRY = "C"  # C for chaos

def main() -> None:
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY, encoding="utf-8")

if __name__ == "__main__":
    main()
