#!/usr/bin/python3
"""
    sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import request as ubr


if __name__ == "__main__":
    new_request = ubr.Request(sys.argv[1])
    with ubr.urlopen(new_request) as response:
        print(dict(response.headers).get("X-Request-Id"))
