import requests

URL = "http://api.open-notify.org/iss-now.json"
request = requests.get(url = URL)
print(request.json())

