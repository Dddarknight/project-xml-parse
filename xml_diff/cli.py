import argparse


def parse():
    parser = argparse.ArgumentParser(
        description='Shows difference between flights in xml')
    parser.add_argument('file1')
    parser.add_argument('file2')
    parser.add_argument('-o', '--output')
    args = parser.parse_args()
    return args
