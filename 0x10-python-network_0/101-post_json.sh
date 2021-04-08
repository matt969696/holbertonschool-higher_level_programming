#!/bin/bash
#sends a POST request to the URL with JSON
curl -sX POST -H "Content-Type: application/json" --data @"$2" "$1"
