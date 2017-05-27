#!/usr/bin/env python

# Make sure to install requests before running:
# > pip install requests
# Documentation for the requests library can be found here: http://docs.python-requests.org/en/master/

import datetime
import requests

class FoodTruckFetcher(object):
    def __init__(self):
        today = _get_weekday()

        self.url = "http://data.sfgov.org/resource/bbb8-hzi6.json?dayorder={}".format(today)
        self.trucks = []

        try:
            self.fetch_trucks()
        except BadResponseError:
            print "Bad response from API. Please try again."

    def __str__(self):
        return "\nNAME     ::     ADDRESS\n------------------------"

    def fetch_trucks(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            truck_data = response.json()
            for raw_truck in truck_data:
                food_truck = FoodTruck(raw_truck['applicant'],
                                    raw_truck['location'],
                                    raw_truck['starttime'],
                                    raw_truck['endtime'])
                if food_truck.open_now():
                    self.trucks.append(food_truck)
            self.trucks.sort(key=lambda truck: truck.name)
            self.print_ten_trucks()
        else:
            raise BadResponseError

    def print_ten_trucks(self):
        print self
        if len(self.trucks) > 10:
            pass
        for truck in self.trucks[0:10]:
            print truck

class FoodTruck(object):
    def __init__(self, name, address, open_time, close_time):
        self.name = name
        self.address = address
        self.open_time = datetime.datetime.strptime(open_time, '%I%p').time()
        self.close_time = datetime.datetime.strptime(close_time, '%I%p').time()

    def __str__(self):
        return "{}, {}".format(self.name, self.address)

    def open_now(self):
        now = datetime.datetime.now().time()
        return now > self.open_time and now < self.close_time

class BadResponseError(Exception):
    pass

def _get_weekday():
    """
    Python's `datetime` module assigns the value of 0 to Monday, while
    the City of SF API assings 0 to Sunday. We need to convert the datetime
    object to a `dayorder` attribute to make a more efficient API call.
    """
    python_weekday = datetime.datetime.now().weekday()
    api_dayorder = (python_weekday + 1) if python_weekday != 0 else 7
    return api_dayorder

if __name__ == "__main__":
    FoodTruckFetcher()
