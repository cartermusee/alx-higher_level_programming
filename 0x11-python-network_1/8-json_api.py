#!/usr/bin/python3
"""module for request package"""
import sys
import requests


if __name__ == "__main__":

    if sys.argv == 1:
        letter = ""
    else:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": letter}

    res = requests.post(url, data=params)

    try:
        dat = res.json()
        if dat:
            print("[{}] {}".format(dat.get("id"), dat.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
