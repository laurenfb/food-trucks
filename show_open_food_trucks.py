import datetime
import requests

class FoodTruckFetcher(object):
    def __init__(self):
        today = _get_weekday()

        self.url = "http://data.sfgov.org/resource/bbb8-hzi6.json?dayorder={}".format(today)
        self.trucks = []
        self.TRUCKS_TO_PRINT = 10

        try:
            self.fetch_trucks()
        except BadResponseError:
            print "Bad response from API. Please try again."

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
            self.print_trucks(self.TRUCKS_TO_PRINT)
        else:
            raise BadResponseError

    def print_trucks(self, number_to_print):
        if self.trucks:
            print "First {} Food Trucks currently open:".format(number_to_print)
            print "NAME      ::     ADDRESS"
            print "------------------------"
            # per spec, print only 10 trucks. even if the list is shorter,
            # using the for loop allows us to avoid throwing an IndexError
            for truck in self.trucks[0:number_to_print]:
                print truck
        else:
            print "No trucks open right now. Sorry!"

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
    the City of SF API assigns 0 to Sunday. We need to convert the datetime
    object to a `dayorder` attribute to make a more efficient API call.
    """
    python_weekday = datetime.datetime.now().weekday()
    api_dayorder = (python_weekday + 1) if python_weekday != 0 else 7
    return api_dayorder

if __name__ == "__main__":
    FoodTruckFetcher()
