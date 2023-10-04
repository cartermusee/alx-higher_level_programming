#!/usr/bin/python3
"""module for request package"""
import requests


res = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("\t-type: {}".format(type(res.text)))
print("\t-content: {}".format(res.text))
