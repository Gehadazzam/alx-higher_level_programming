#!/usr/bin/python3
"""
    sends a request to the URL and displays
    the value of the X-Request-Id variable found in the header of the response.
"""
import sys
import requests as r


if __name__ == "__main__":
    new_request = r.get(sys.argv[1])
    print(new_request.headers.get("X-Request-Id"))
