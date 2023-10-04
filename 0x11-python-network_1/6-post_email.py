#!/usr/bin/python3
"""module for request package"""
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = {"email":argv[2]}
    res = requests.post(url, data=email)
    print(res.text)
