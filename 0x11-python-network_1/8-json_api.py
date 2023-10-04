#!/usr/bin/python3
"""module for request package"""
import requests
import sys


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) == 1:
        lq = ""
    else:
        lq = sys.argv[1]
    par = {"q": lq}
    res = requests.post(url, data=par)
    try:
        res_json = res.json()

        if res_json:
            print("{[]} {}".format(res_json['id'], res_json['name']))
        else:
            print("No results")
    except ValueError:
        print("Not a valid JSON")
