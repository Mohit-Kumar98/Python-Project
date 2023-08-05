# newtork ke through api call kar sakte hai.
import requests
import json
import os

city=input("Enter the name of your city: ")
url=f"https://api.weatherapi.com/v1/current.json?key=e061972af4e048c0b6c05737230508&q={city}"
r=requests.get(url)
# use to parse string to dictionary
wdic=json.loads(r.text)
#we are accessing data from dictionary
speak=wdic["current"]["temp_c"]
command=f"say The current weather in {city} is {speak} degrees"
os.system(command)



