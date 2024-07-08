import requests
import pandas as pd
import json
from datetime import datetime, timedelta

statename = "delhi"
startdate = datetime(2024, 5, 1)
enddate = datetime(2024, 6, 30)
datalist = []


def get_data(data_string):
    link = f"https://vegetablemarketprice.com/api/dataapi/market/delhi/daywisedata?date={date_str}"

    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
        "sec-ch-ua": "\"Not/A)Brand\";v=\"8\", \"Chromium\";v=\"126\", \"Google Chrome\";v=\"126\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "cookie": "JSESSIONID=7DCA83AF88D74F763774905CD5EA0D43; _ga=GA1.1.579592366.1719805178; __gads=ID=d417311b4ca58bd6:T=1719805164:RT=1719805164:S=ALNI_MZBDVVGHlSQqR5k0P8vj4Ymc9foyA; __gpi=UID=00000e6d610639a0:T=1719805164:RT=1719805164:S=ALNI_MbOlZIJQSQMot2btmDNHhDbbUpTNw; __eoi=ID=5fb93107935acbae:T=1719805164:RT=1719805164:S=AA-Afjbak2cMxgawT7R_UvUzAL3n; _ga_2RYZG7Y4NC=GS1.1.1719805178.1.1.1719805217.0.0.0; FCNEC=%5B%5B%22AKsRol-OtelDtdCW5TTRX5DbcCTw22YeR7qeIawMoDe0pq8Ub6oK3fFXUeH0X7oqPSXfmcdd2HxA2Y7INCAKWHjyvMmu2YDvGQWNtlmZ702PZ6WqWITxix-3mZbovWDBeVg44JknSd9CzIx7g6NDK3Ks4_CbT5hW0Q%3D%3D%22%5D%5D",
        "Referer": "https://vegetablemarketprice.com/market/delhi/today",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Referrer-Policy": "strict-origin-when-cross-origin"
    }

    response = requests.get(link, headers=headers)
    if response.status_code == 200:
        js_data = response.json()
        for item in js_data.get("data", []):
            datalist.append({
                "date": date_str,
                "state_name": "delhi",
                "vegetable_name": item.get("vegetablename"),
                "wholesale_price": item.get("price"),
                "retail_price": item.get("retailprice"),
                "shoping_mall_price": item.get("shopingmallprice"),
                "unit": item.get("units"),
                "image":"https://vegetablemarketprice.com/"+item.get("table").get("chart_symbol")
            })
#getting the data
while startdate <= enddate:
    date_str = startdate.strftime("%Y-%m-%d")
    startdate += timedelta(days=1)
    get_data(date_str)

#converting the data into dataframe and storing it as a csv file
df = pd.DataFrame(datalist)
df.to_csv("main.csv", index=False)
print("Data saved to main.csv")
  
  