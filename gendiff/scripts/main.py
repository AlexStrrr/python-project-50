#!/usr/bin/env python


import argparse
from gendiff.run.gendiff import generate_diff


def cli():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default="stylish",
                        help='set format of output ("Plain" '
                             'or "JSON" or default: "stylish")')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    first_file, second_file, format_name = cli()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == '__main__':
    main()
