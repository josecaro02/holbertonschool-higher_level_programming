#!/bin/bash
# Displays size of the body response
curl -sI 0.0.0.0:5000 | awk '/Content-Length:/{print $2;}'
