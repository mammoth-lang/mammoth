import sys
import tomllib
from pathlib import Path


def has_config():
    return Path("mammoth.toml").is_file()


def get_config():
    if not has_config():
        print("Not in a Mammoth project: No mammoth.toml found")
        sys.exit(1)

    with open("mammoth.toml", "rb") as f:
        data = tomllib.load(f)

    return data
