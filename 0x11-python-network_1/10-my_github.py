#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials (username and
    password) and uses the GitHub API to display your id
"""
import requests as r
from requests.auth import HTTPBasicAuth as ath
from sys import argv as av

if __name__ == "__main__":
    checker = ath(av[1], av[2])
    new_request = r.get("https://api.github.com/user", auth=checker)
    print(new_request.json().get("id"))
