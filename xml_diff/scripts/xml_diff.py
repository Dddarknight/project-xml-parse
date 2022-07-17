#!/usr/bin/env python

from xml_diff.parsing import parsing
from xml_diff.diff import xml_difference


def main():
    args = parsing()
    xml_difference(
        args['file1'], args['file2'], output=args['output'])


if __name__ == '__main__':
    main()
