#!/usr/bin/python3
"""module for request"""


import urllib.request
from sys import argv


if __name__ == "__main__":
    reg = urllib.request.Request(argv[1])
    with urllib.request.urlopen(reg) as response:
        if 'X-Request-Id' in response.headers:
            res_id = response.headers['X-Request-Id']
            print("{}".format(res_id))
