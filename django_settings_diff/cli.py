#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""docstring"""

import argparse

from .settingsdiff import dump_settings, diff_settings


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("settings_path_1", nargs="?")
    parser.add_argument("settings_path_2", nargs="?")
    parser.add_argument("-d", "--dump")
    args = parser.parse_args()

    if args.dump:
        dump_settings(args.dump)
    elif args.settings_path_1 and args.settings_path_2:
        diff_settings(args.settings_path_1, args.settings_path_2)
    else:
        parser.error("Invalid argument configuration!")


if __name__ == '__main__':
    main()
