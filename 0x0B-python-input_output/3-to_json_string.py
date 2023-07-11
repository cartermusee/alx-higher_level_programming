#!/usr/bin/python3
import json
"""module for json"""


def to_json_string(my_obj):
    text = json.dumps(my_obj)
    return text
