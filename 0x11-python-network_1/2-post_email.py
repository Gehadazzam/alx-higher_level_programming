#!/usr/bin/python3
"""
    sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import request as ubr
from urllib.parse import urlencode as enc

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    new_request = ubr.Request(sys.argv[1], enc(email).encode("ascii"))
    with ubr.urlopen(new_request) as response:
        print(response.read().decode("utf-8", "replace"))
