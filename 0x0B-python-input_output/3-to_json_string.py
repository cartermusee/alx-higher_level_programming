#!/usr/bin/python3
"""module for json"""
import json


def to_json_string(my_obj):
    text = json.dumps(my_obj)
    return text
