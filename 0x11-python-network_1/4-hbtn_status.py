#!/usr/bin/python3
"""fetch url"""
import requests as r

if __name__ == "__main__":
    """Your code should not be executed when imported"""
    new_request = r.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(new_request.text)))
    print("\t- content: {}".format(new_request.text))
