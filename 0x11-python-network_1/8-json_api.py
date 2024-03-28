#!/usr/bin/python3
"""
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""
from sys import argv as av
import requests as r


if __name__ == "__main__":
    if len(av) == 1:
        arg = ""
    else:
        arg = av[1]
    new_request = r.post(
        "http://0.0.0.0:5000/search_user", {"q", arg})
    try:
        response = new_request.json()
        if response == {}:
            print("No result")
        else:
            print(f"[{response.get("id")}] {response.get("name")}")
    except ValueError:
        print("Not a valid JSON")
