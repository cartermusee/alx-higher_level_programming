#!/usr/bin/python3
"""python module for auth"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    """the main func"""

    auth = HTTPBasicAuth(sys.argv[1],sys.argv[2])
    response = requests.get("https://api.github.com/user",auth=auth)
    print(response.json().get("id"))
