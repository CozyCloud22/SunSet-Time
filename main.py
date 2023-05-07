import config
import requests
import datetime
import pytz

api_key = config.API_KEY

#change to user input
city = "East Lansing"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#recieving responses from the api
response = requests.get(url)
data = response.json()

timeZoneOff = response.json()["timezone"]
timeDiff = timeZoneOff / 3600

sunrise = data["sys"]["sunset"]

#converts the sunset time to a time that 
convertReg = datetime.datetime.utcfromtimestamp(sunrise)
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
print(finalAns)