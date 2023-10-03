#!/usr/bin/python3
"""module for post"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            res_body = response.read().decode("utf-8")
            print(res_body)
    except urllib.error.HTTPError as e:
        print(e.code)
