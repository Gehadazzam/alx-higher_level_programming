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
    char = {'q': arg}
    link = 'http://0.0.0.0:5000/search_user'
    responce = r.post(link, char)
    try:
        json_responce = responce.json()
        if json_responce == {}:
            print("No result")
        else:
            print("[{}] {}".format(
                json_responce.get('id'), json_responce.get('name')
            ))
    except ValueError:
        print("Not a valid JSON")
