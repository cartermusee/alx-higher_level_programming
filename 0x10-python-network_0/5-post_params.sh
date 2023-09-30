#!/bin/bash
#Bash script that takes in a URL, sends a POST request to
curl -s -Xd POST "email=test@gmail.com&subject=I will always be here for PLD" "$1"
