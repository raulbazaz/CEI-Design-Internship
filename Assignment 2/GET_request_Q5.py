import requests

URL = "http://api.open-notify.org/iss-now.json"
request = requests.get(url = URL)
data = request.json()
Latitude = data['iss_position']['latitude']
Longitude = data['iss_position']['longitude']
Time_Stamp = data['timestamp']

print(Latitude,Longitude,Time_Stamp)
