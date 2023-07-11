#!/usr/bin/python3
"""module for dumb in json"""
import json


def save_to_json_file(my_obj, filename):
    """function to to text using json rep"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
