#!/bin/bash
#makes a request
curl -o /dev/null -s -Lw "You got me!" 0.0.0.0:5000/catch_me
