import config
import requests
import datetime
import pytz

api_key = config.API_KEY

#user input
city = input("Enter the city you want: ")
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#recieving responses from the api
response = requests.get(url)
data = response.json()

timeZoneOff = response.json()["timezone"]
timeDiff = timeZoneOff / 3600

sunset = data["sys"]["sunset"]

#converts the sunset time to a time that I can use
convertReg = datetime.datetime.utcfromtimestamp(sunset)
timern = convertReg.strftime("%H:%M:%S")
toChange = timern[0:2]

#calculates time zone difference
if(toChange == "00"):
    toChange = "12"
temp = int(toChange)
temp += int(timeDiff)

if(temp < 1):
    temp += 12
subBackIn = str(temp)
finalAns = subBackIn + timern[2:-3] + " pm"

#prints answer
print(f"The sun will set in {city} at {finalAns}")