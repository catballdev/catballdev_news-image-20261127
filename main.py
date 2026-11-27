#!/usr/bin/env python3
"""Main entry point for the news-image project."""

import os
import shutil
from pathlib import Path

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