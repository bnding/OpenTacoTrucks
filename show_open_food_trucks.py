import requests
import datetime
import json

# Getting data from website. Converting to json
def getData():
    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"

    response = requests.get(url)

    # HTTP status code. 200 = "OK" (server succesfully answered http request)
    if response.status_code == 200:
        data = response.json()

    return data

# Converting all times in 24hr format to datetime object. Helper method for list comprehension
def getTruckHours(time):
    now = datetime.datetime.now()

    # timedate library only supports 0-23 time. API however ends at 24:00. Need to convert the time to next day at 0:00
    if time == "24:00":
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        now += datetime.timedelta(days=1)
        return now

    # Combining time and date. Need to convert the time first to datetime object and then combining.
    # Only updating time will result in date to be 1900-01-01
    time = datetime.datetime.strptime(time, "%H:%M").time()
    now = datetime.datetime.combine(now.date(), time)
    return now

# Filtering through json. Creating new variable that shows currently open food trucks
def getOpenTrucks(data):
    # Getting current day and time to satisfy API standard
    today = datetime.datetime.now()

    # !!! To test, change the currentTime to something else. You can also add the parameter "day={integer}" for different days. However, make sure to change the day in getTruckHours() (line 24 and after line 32)
    # today = today.replace(hour=23, minute=30, second=0, microsecond=0)

    # %w = weekday as a number 0-6... 0 is Sunday
    currentDay = today.strftime("%w")

    # List comprehension for filtering. openTrucks will contain trucks that are currently open on that day
    openTrucks = [x for x in data
                # Getting trucks open on current day
                  if ((currentDay == x['dayorder']) and
                # Getting all trucks open after after the current time and before the closing time
                  (getTruckHours(x['start24']) <= today) and
                  (getTruckHours(x['end24']) > today))
                  ]

    # Applying lambda function to sort truck names alphabetically
    openTrucks.sort(key=lambda x: x['applicant'])
    return openTrucks

# Printing trucks every 10 times
def printTrucks(trucks):
    count = 0
    for truck in trucks:
        if (count % 10 == 0 and count > 0):
            input("\n\nPress enter to list next 10 trucks\n\n")
        print(f"{truck['applicant']} at {truck['location']}. Closing at {truck['endtime']}.")

        count+=1
    print("\n\nAll trucks are now listed.")

# Excecuting code here
def main():
    mainData = getData()
    openTrucks = getOpenTrucks(mainData)

    if(openTrucks == [] or openTrucks == None):
        print("No food trucks currently available.")
    else:
        print("\nPrinting currently open food trucks...\n\n")
        printTrucks(openTrucks)

if __name__ == '__main__':
    main()