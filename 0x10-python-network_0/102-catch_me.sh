#!/bin/bash
# Catched or not catched
curl -LX PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
