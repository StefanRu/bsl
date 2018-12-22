import pandas as pd
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from influxdb import InfluxDBClient

res = requests.get("https://www.euroairport.com/en/passengers-visitors/arrivals-departures/flights/departures.html")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0]

table_rows = table.find_all('tr')

json_body = [
    {
        "measurement": "departure",
        "tags": {
            "airport": "bsl"
            },
        "time": datetime.datetime.now().isoformat(),
        "fields": {
            "Float_value": 0.64,
            "Int_value": 3,
            "String_value": "Text",
            "Bool_value": True
        }
    }
]

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    print(row)


df = pd.read_html(str(table))

with open('/home/stefan/bsl/departures.html', 'w' ) as f:
 print( tabulate(df[0], headers='keys', tablefmt='html'),file=f )

df_departures, = pd.read_html('/home/stefan/bsl/departures.html',header=0)
with open('/home/stefan/bsl/departures.json', 'w' ) as f:
 print(df_departures.to_json(orient='table'),file=f)

client = InfluxDBClient(host='localhost', port=8086)
client.switch_database('bsl')

client.write_points(df_departures.to_json(orient='records'))
