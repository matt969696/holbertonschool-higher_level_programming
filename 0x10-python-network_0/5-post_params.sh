#!/bin/bash
#sends a POST request to the URL with arg
curl -sX POST -d 'email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD' "$1"
