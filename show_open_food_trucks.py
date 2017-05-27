#!/usr/bin/env python

# Make sure to install requests before running:
# > pip install requests
# Documentation for the requests library can be found here: http://docs.python-requests.org/en/master/

import datetime
import requests

class FoodTruckFetcher(object):
    def __init__(self):
        self.url = "http://data.sfgov.org/resource/bbb8-hzi6.json"
        self.now = datetime.datetime.now()

# response = requests.get(url)
# if response.status_code == 200:
#     data = response.json()

if __name__ == "__main__":
    FoodTruckFetcher()
