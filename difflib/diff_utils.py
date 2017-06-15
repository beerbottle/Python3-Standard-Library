#!/usr/bin/env python3
""" Command line interface to difflib.py providing diffs in four formats:

* ndiff:    lists every line and highlights interline changes.
* context:  highlights clusters of changes in a before/after format.
* unified:  highlights clusters of changes in an inline format.
* html:     generates side by side comparison with change highlights.

"""

import sys
import os
import difflib
import argparse
from datetime import datetime, timezone


def file_mtime(path):
    t = datetime.fromtimestamp(os.stat(path).st_mtime, timezone.utc)
    return t.astimezone().isoformat()


def main():
    parser = argparse.ArgumentParser()


if __name__ == '__main__':
    print(file_mtime(__file__))
    print(__file__)
