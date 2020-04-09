#!/bin/bash
# Make a POST request using as paremeter a file json
curl -sH "Content-Type: application/json" -d "@$2" "$1"
