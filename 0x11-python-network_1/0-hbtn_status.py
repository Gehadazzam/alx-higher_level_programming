#!/usr/bin/python3
"""fetch url"""
import urllib.request as ur

if __name__ == "__main__":
    """Your code should not be executed when imported"""

    new_request = ur.Request("https://alx-intranet.hbtn.io/status")
    with ur.urlopen(new_request) as response:
        text = response.read()
        print("Body response:")
        print("\t- type: {type(text)}")
        print(f"\t- content: {text}")
        print("\t- utf8 content:", text.decode("utf-8"))
