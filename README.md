# a little bit about `food-trucks`

This short project makes use of one of the San Francisco city government's OpenData APIs. With a simple API call, it finds food trucks in San Francisco that are open for business at the date and time the program is run. By default, the program will print the first 10 trucks, sorted alphabetically, that are open at the time. If more trucks are desired, changing the constant `self.TRUCKS_TO_PRINT` in the `FoodTruckFetcher` is simple. If no trucks are open, or if a poor response is returned from the API, the program makes that clear to the user with a useful error message.

# how to install & run `food-trucks`

To run this simple command-line program, first clone it from github:

`git clone https://github.com/laurenfb/food-trucks.git`

Next, we need a virtual environment to install the dependencies that this program relies on. First, use `pip` to install `virtualenv` if you do not already have it.

`pip install virtualenv`

Create your virtual environment. Make sure you are in the main directory of this project (most likely called `food-trucks` unless you renamed it) and run:

`virtualenv venv`

If you plan to contribute to this repo, it's probably convenient to keep your virtual environment named `venv` (as opposed to `myvenv` or `charlie` or anything more interesting), as git ignores that name.

Next, install the dependencies from the requirements file and activate your virtual environment.

`pip install -r requirements.txt`

`source venv/bin/activate`

Make sure the name of your virtual environment -- `venv` in this case -- matches the name of the virtual environment you created above.

Finally, run the program to get the food trucks you desire! Food is moments away.

`python show_open_food_trucks.py`

# what i'd do differently next time

If I were building this service as a full-scale application, there are a few ways to optimize. To ensure a speedy response for users and to take advantage of the fact that food trucks tend to open and close on the hour, I would run the food truck fetcher script in the background and cache the results. Since food trucks are rarely likely to close at, for instance, 11:42 am, an optimized app could easily run the algorithm at 11:01 and be reasonably sure the results are accurate. This may not be necessary during off-hours that aren't near mealtimes, but could definitely improve load balancing during the busy lunch and dinner hours.

Another thing that would make a larger application more user-friendly would be grouping trucks with the same name. In many instances, multiple trucks with the same business name come back from the API. Grouping those into a single entry, even if they are at different physical locations, would allow the user to see more available food trucks on a page of 10. Finally, as a cherry on top, adding location services would be an additional way to improve user experience, since users are often looking for food near to them.
