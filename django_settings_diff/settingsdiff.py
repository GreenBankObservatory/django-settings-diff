# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import pickle
from pprint import pprint

from deepdiff import DeepDiff


def dump_settings(dump_path, dump_type):
    """Given an output path, dump the given settings as a .pkl file"""
    import os
    import sys

    sys.path.insert(0, os.path.realpath("."))
    import django

    django.setup()
    from django.conf import settings

    settings_dict = settings.__dict__["_wrapped"].__dict__

    if not dump_type:
        dump_type = dump_path.split(".")[-1]
    with open(dump_path, "w") as file:
        if dump_type == "txt":
            pprint(settings_dict, stream=file)
        elif dump_type == "pkl":
            pickle.dump(settings_dict, file)
        else:
            raise NotImplementedError(
                "Dump type '{}' is not supported (derived from dump path '{}')! "
                "Specify dump_type explicitly to resolve this.".format(dump_type, dump_path)
            )


def load_settings(path):
    """Unpickle the given input file"""
    with open(path) as file:
        return pickle.load(file)


def diff_settings(path1, path2):
    """Given the paths to two pickled settings dicts, load them up and diff them"""
    settings1 = load_settings(path1)
    settings2 = load_settings(path2)
    pprint(DeepDiff(settings1, settings2, exclude_paths={"root['_explicit_settings']"}))
