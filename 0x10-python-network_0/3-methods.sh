#!/bin/bash
#displays all HTTP methods
curl -sI Allow "$1" -L| grep "Allow" | cut -d " " -f2-
