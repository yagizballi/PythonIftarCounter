import requests
import json
from datetime import datetime

url = "https://aladhan.p.rapidapi.com/timingsByCity"

querystring = {"country": "TUR", "city": "Istanbul"} # "country": "A country name or ISO 2 digit aplha code, like 'US' or 'United States of America'", "city": "A city name, like 'Istanbul'"

headers = {
    "X-RapidAPI-Key": "Your rapidapi.com key",
    "X-RapidAPI-Host": "aladhan.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

json_data = json.loads(response.text)
sunset = json_data['data']['timings']['Sunset']

time_str = sunset
hour, minute = map(int, time_str.split(":"))

now = datetime.now()
current_hour = now.hour
current_minute = now.minute

remaining_hour = hour - current_hour
remaining_minute = minute - current_minute
if remaining_minute < 0:
    remaining_hour -= 1
    remaining_minute += 60
if remaining_hour < 0:
    remaining_hour += 24
print("{:02d} hour, {:02d} minute until Iftar.".format(remaining_hour, remaining_minute)) # There may be a margin of error of couple minutes. In this case, you can add or subtract a few minutes for fix the time. Example; {remaining_minute + 1}