#!/usr/bin/env python


import argparse
from gendiff.run.gendiff import generate_diff
from gendiff.formatters.all_formatters import DEFAULT_FORMAT, FORMATS


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='Generate diff looking for differences '
                    'in two configuration files and shows a difference.')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format',
                        help='set format of output (default: stylish)',
                        choices=FORMATS,
                        default=DEFAULT_FORMAT)

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    first_file, second_file, format_name = parse_arguments()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == '__main__':
    main()
