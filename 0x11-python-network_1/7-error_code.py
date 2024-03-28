#!/usr/bin/python3
"""
     sends a request to the URL and displays the body of the response
"""
from sys import argv as av
import requests as r

if __name__ == "__main__":
    new_request = r.get(av[1])
    if new_request.status_code < 400:
        print(new_request.text)
    else:
        print(f"Error code: {new_request.status_code}")
