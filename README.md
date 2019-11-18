#Open Taco Trucks using Command Line

Project is complete using Python3.

##Dependencies
* requests
* datetime
* json

##Program Build


##Running the Program
`python3 show_open_food_trucks.py`

###Running this on Sunday 10:38PM gave me the following code:

	Printing currently open food trucks...


	Bay Area Dots, LLC 567 BAY ST
	Bay Area Dots, LLC 900 BEACH ST
	San Francisco Street Foods, Inc. 5 THE EMBARCADERO
	San Francisco Street Foods, Inc. 2 MONTGOMERY ST
	San Francisco Street Foods, Inc. 1 THE EMBARCADERO
	San Francisco Street Foods, Inc. 100 POST ST
	San Francisco Street Foods, Inc. 701 HOWARD ST
	San Francisco's Hometown Creamery 281 GEARY ST
	Wu Wei LLC dba MoBowl 370 DRUMM ST


	All trucks are now listed.

##Testing code for different time and day

####Changing the time
In the function `getOpenTrucks(data)` call the function `today.replace()` at the line after declaring `today = datetime.datetime.now()`

`today = today.replace(hour=23, minute=30, second=0, microsecond=0)`

Will change the time to 11:30PM

####Changing the day
**It is very important that we change the day in both functions `getOpenTrucks(data)` and `getTruckHours(time)`**


In the function **`getOpenTrucks(data)`**, add the parameter `day={integer}` to `today.replace `after declaring `today =  datetime.datetime.now()` such that `integer` is a value from **0 (Sunday)** to **6 (Saturday)**

In the function **`getTruckHours(time)`**, call `now.replace(day={integer})` after declaring the variable `now = datetime.datetime.now()`

So if we wanted to see what is open on Friday (day = 5) at 6:30PM...

`today = today.replace(hour=18, minute=30, second=0, microsecond=0, day=5)`

`now = now.replace(day=5)`

would be added at the their respective locations.

[click here for datetime library](https://docs.python.org/2/library/datetime.html)
