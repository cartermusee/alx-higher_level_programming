#!/usr/bin/python3
"""module for post"""
import urllib.request
import urllib.parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode("ascii")
    req = urllib.request.Request(url,data)
    with urllib.request.urlopen(req) as response:
        res_body = response.read().decode("utf-8")
        print("Your email is: {}".format(res_body))
