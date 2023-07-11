#!/usr/bin/python3
"""module for load in json"""
import json


def load_from_json_file(filename):
    """function to creates an Object from a jSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        return json.load(f)
