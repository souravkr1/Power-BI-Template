#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

def duplicate_pbit(src_file: str, new_names: list[str], output_dir: str = "."):
    src = Path(src_file)
    if not src.exists():
        raise FileNotFoundError(f"Template not found: {src}")
    if src.suffix.lower() != ".pbit":
        raise ValueError("Source file must be a .pbit")

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    created = []
    for name in new_names:
        new_file = out_dir / f"{name}.pbit"
        shutil.copy2(src, new_file)
        created.append(str(new_file))
        print(f"Created: {new_file}")
    return created


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Duplicate a Power BI template (.pbit) into new files with new names"
    )
    parser.add_argument("source", help="Path to source .pbit file")
    parser.add_argument("names", nargs="+", help="New file base names (without .pbit)")
    parser.add_argument("-o", "--output", default=".", help="Output directory (default: current dir)")
    args = parser.parse_args()

    duplicate_pbit(args.source, args.names, args.output)
