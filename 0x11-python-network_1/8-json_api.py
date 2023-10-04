#!/usr/bin/python3
"""module for request package"""
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(argv) > 1:
        lq = argv[1]
    else:
        lq = ""
    par = {"q": lq}
    try:
        res = requests.post(url, data=par)
        res_json = res.json()

        if res_json:
            print("{[]} {}".format(res_json['id'], res_json['name']))
        else:
            print("No results")
    except ValueError:
        print("Not a valid JSON")
