#!/usr/bin/env python3
"""Main entry point for the news-image project."""

import os
import shutil
import sys
from pathlib import Path

def print_usage():
    print("Usage: python3 main.py [--help]")
    print("  --help    Show this help message and exit.")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print_usage()
        sys.exit(0)

    # Locate entry.png next to main.py itself
    source = Path(__file__).resolve().parent / "entry.png"

    # Output directory from environment variable
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = Path(output_dir)

    # Create output directory if needed
    output_path.mkdir(parents=True, exist_ok=True)

    # Copy entry.png to <output dir>/entry.png (byte-for-byte copy)
    destination = output_path / "entry.png"
    shutil.copyfile(source, destination)

    print(f"Copied {source} to {destination}")

if __name__ == "__main__":
    main()