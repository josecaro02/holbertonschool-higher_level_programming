#!/bin/bash
# Prints all HTTP methods the server will accept
curl -sI "$1" | awk '/Allow:/{print;}' | cut -d' ' -f2-
