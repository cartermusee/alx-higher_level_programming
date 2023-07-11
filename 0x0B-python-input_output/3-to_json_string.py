#!/usr/bin/python3
"""module for json"""
import json


def to_json_string(my_obj):
    """function to return json"""
    text = json.dumps(my_obj)
    return text
