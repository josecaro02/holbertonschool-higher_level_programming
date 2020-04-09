#!/bin/bash
# Displays size of the body response
curl -sI "$1" | awk '/Content-Length:/{print $2;}'
