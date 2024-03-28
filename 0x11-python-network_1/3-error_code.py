#!/usr/bin/python3
"""
     sends a request to the URL and displays the body of the response
"""
from sys import argv as av
from urllib import request as ubr
from urllib.error import HTTPError

if __name__ == "__main__":
    new_request = ubr.Request(av[1])
    try:
        with ubr.urlopen(new_request) as response:
            print(response.read().decode("ascii"))
    except HTTPError as hte:
        print(f"Error code: {hte.code}")
