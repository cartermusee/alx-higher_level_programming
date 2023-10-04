#!/usr/bin/python3
"""module for request package"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if res.status_code >= 400:
        print("Error code: {}".format(res.status_code))
