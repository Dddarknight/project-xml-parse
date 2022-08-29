#!/usr/bin/env python

from xml_diff.cli import parse
from xml_diff.files_diff import xml_difference


def main():
    args = parse()
    xml_difference(
        args.file1, args.file2, output=args.output)


if __name__ == '__main__':
    main()
