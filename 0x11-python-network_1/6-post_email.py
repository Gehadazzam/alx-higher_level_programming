#!/usr/bin/python3
"""
    sends a POST request to the passed URL with the email as a parameter,
    and displays the body of the response
"""
import sys
import requests as r

if __name__ == "__main__":
    email = {"email": sys.argv[2]}
    new_request = r.post(sys.argv[1], email)
    print(new_request.text)
