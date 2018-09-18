#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring"""

from __future__ import print_function, unicode_literals
import argparse
import sys

from .settingsdiff import dump_settings, diff_settings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "settings_path_1",
        nargs="?",
        help='The path to the .pkl file of the first (i.e. "original") settings dump',
    )
    parser.add_argument(
        "settings_path_2",
        nargs="?",
        help='The path to the .pkl file of the second (i.e. "new") settings dump',
    )
    parser.add_argument(
        "-d", "--dump", metavar="PATH", help="The path the settings will be dumped to"
    )
    parser.add_argument(
        "-t",
        "--dump-type",
        choices=["txt", "pkl"],
        help=(
            "The file type of the dump. Only needed if type cannot be derived "
            "from extension give via --dump"
        ),
    )
    args = parser.parse_args()

    if args.dump:
        try:
            dump_settings(args.dump, args.dump_type)
        except NotImplementedError as error:
            print("ERROR: {}".format(error), file=sys.stderr)
            sys.exit(1)
    elif args.settings_path_1 and args.settings_path_2:
        diff_settings(args.settings_path_1, args.settings_path_2)
    else:
        parser.error("Invalid argument configuration!")


if __name__ == "__main__":
    main()
