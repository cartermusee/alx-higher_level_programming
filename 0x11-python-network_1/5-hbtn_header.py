#!/usr/bin/python3
"""module for request package"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    res = requests.get(url)
    if "X-Request-Id" in res.headers:
        x_id = res.headers['X-Request-Id']
        print(x_id)
