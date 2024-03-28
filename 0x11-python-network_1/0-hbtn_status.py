#!/usr/bin/python3

import urllib.request as ur

if __name__ == "__main__":
    new_request = ur.Request("https://alx-intranet.hbtn.io/status")
    with ur.urlopen(new_request) as response:
        text = response.read()
        print("Body response:")
        print("\t- type: {type(text)}")
        print(f"\t- content: {text}")
        print("\t- utf8 content:", text.decode("utf-8"))
