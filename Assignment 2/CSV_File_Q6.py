import requests
import pandas as pd
import time

def isslocation():
    URL = "http://api.open-notify.org/iss-now.json"
    request = requests.get(url = URL)
    data = request.json()
    return {
    "Time_Stamp" : data['timestamp']
    }


arr = []

for i in range(100):
    api = isslocation()
    arr.append(api)
    time.sleep(1)
    print(arr)

dataframe = pd.DataFrame(arr)
dataframe.to_csv("iss_location.csv")
print("csv file created")

