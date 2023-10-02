#!/usr/bin/python3
"""module for request"""


import urliib.request


if __name__ == "__main__":
    reg = urllib.requestRequest("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen(reg) as res:
        res = response.read()

        print("Body response:$")
        print("\t- type: {}".formta(type(res)))
        print("\t- content: {}".formta(res))
        print("\t- utf8 content: {}".formta(res.decode("utf-8")))
