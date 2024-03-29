#!/usr/bin/python3
"""
    takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
"""
from sys import argv as av
import requests as r


if __name__ == "__main__":
    new_request = r.get(
        "https://api.github.com/repos/{}/{}/commits".format(av[2], av[1]))
    commit = new_request.json()
    try:
        for num in range(10):
            print("{}: {}".format(
                commit[num].get("sha"),
                commit[num].get("commit").get("author").get("name")))
    except IndexError:
        pass
