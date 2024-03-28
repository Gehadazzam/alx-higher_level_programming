#!/usr/bin/python3
"""
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response
"""
import sys
from urllib import request as ubr
from urllib.parse import urlencode as enc

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    new_request = ubr.Request(sys.argv[1], enc(email).encode("ascii"))
    with ubr.urlopen(new_request) as response:
        print(response.read().decode("utf-8", "replace"))
