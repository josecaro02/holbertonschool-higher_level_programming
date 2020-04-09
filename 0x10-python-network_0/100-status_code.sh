#!/bin/bash
# Prints http_code response of a request
curl -w "%{Http_code}" -s -o /dev/null -L "$1"
