#!/bin/bash
# Prints response of a get request if http_code is 200
status_code=$(curl -w "%{Http_code}" -s -o /dev/null -L "$1")
if [ "$status_code" -eq 200 ]
then
    curl -sL "$1"
fi
