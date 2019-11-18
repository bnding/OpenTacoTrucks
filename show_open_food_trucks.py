import requests
import datetime
import json

# Getting data from website. Converting to json
def getData():
    url = "http://data.sfgov.org/resource/bbb8-hzi6.json"

    response = requests.get(url)

    # HTTP status code. 200 = "OK", else error
    if response.status_code == 200:
        data = response.json()
    else:
        data = []

    return data

# Getting all truck times to datetime object
def getTruckHours(time):
    now = datetime.datetime.now()

    # Creating datetime object for truck database w/ 24:00
    if time == "24:00":
        now = now.replace(hour=0, minute=0, second=0, microsecond=0)
        now += datetime.timedelta(days=1)
        return now

    # Creating datetime object for truck database w/ no 24:00
    time = datetime.datetime.strptime(time, "%H:%M").time()
    now = datetime.datetime.combine(now.date(), time)
    return now

# Filtering through json. Creating new variable that shows currently open food trucks
def getOpenTrucks(data):
    today = datetime.datetime.now()

    # %w = weekday as a number 0-6... 0 is Sunday
    currentDay = today.strftime("%w")

    # Using list comprehension to get currently open trucks
    openTrucks = [x for x in data
                  if ((currentDay == x['dayorder']) and
                  (getTruckHours(x['start24']) <= today) and
                  (getTruckHours(x['end24']) > today))
                  ]

    # Applying lambda function to sort truck names alphabetically
    openTrucks.sort(key=lambda x: x['applicant'])
    return openTrucks

def printTrucks(trucks):
    count = 0
    for truck in trucks:
        if (count % 10 == 0 and count > 0):
            input("\n\nPress enter to list next 10 trucks\n\n")
        print(f"{truck['applicant']} {truck['location']}")

        count+=1
    print("\n\nAll trucks are now listed.")

def main():
    mainData = getData()
    if(mainData == []):
        print("Error requesting data from site. Please check if url is correct or try again later.")
        return

    openTrucks = getOpenTrucks(mainData)

    if(openTrucks == [] or openTrucks == None):
        print("No food trucks currently available.")
    else:
        print("\nPrinting currently open food trucks...\n\n")
        printTrucks(openTrucks)

if __name__ == '__main__':
    main()