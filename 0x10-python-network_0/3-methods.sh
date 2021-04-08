#!/bin/bash
#displays the size of the body of the response
curl -si -X OPTIONS "$1" | grep Allow | cut -d ' ' -f2-
