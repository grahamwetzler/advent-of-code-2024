import sys
from pathlib import Path


def get_input():
    day = Path(sys.argv[0]).stem
    return Path(f"input/{day}.txt").read_text()
