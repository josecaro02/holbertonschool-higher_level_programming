#!/usr/bin/python3
import json


def load_from_json_file(filename):

    with open(filename, 'r', encoding="utf-8") as f:
        return (json.load(f))
