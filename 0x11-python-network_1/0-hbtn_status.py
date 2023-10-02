#!/usr/bin/python3
"""module for request"""


import urliib


if __name__ == "__main__":
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        res = response.read()

        print("Body response:$")
        print("\t- type: {}".formta(type(res)))
        print("\t- content: {}".formta(res))
        print("\t- utf8 content: {}".formta(res.decode("utf-8")))
