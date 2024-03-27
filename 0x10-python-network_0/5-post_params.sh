#!/bin/bash
#sends a POST request to the passed UR
curl -sX POST "$1" -L  -d "email=test@gmail.com&subject=I will always be here for PLD"
