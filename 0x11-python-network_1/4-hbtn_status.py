#!/usr/bin/python3
"""module for request package"""
import requests


res = requests.get('https://alx-intranet.hbtn.io/status')
print("Body response:")
print("- type: {}".format(type(res.text)))
print("- content: {}".format(res.text))
