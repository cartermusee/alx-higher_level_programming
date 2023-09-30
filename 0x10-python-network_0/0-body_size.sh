#!/bin/bash
#Bash script that takes in a URL, sends a request
echo $(curl -s "$1")
