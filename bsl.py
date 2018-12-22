import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from xml.etree import ElementTree as ET
from tabulate import tabulate
from influxdb import InfluxDBClient


res = requests.get("https://www.euroairport.com/en/passengers-visitors/arrivals-departures/flights/departures.html")
soup = BeautifulSoup(res.content,'lxml')
#table = soup.find_all('table')[0]
s = soup.find('table', attrs={'class':'mytable'}).get_text()

table = ET.XML(s)
rows = iter(table)
headers = [col.text for col in next(rows)]
for row in rows:
    values = [col.text for col in row]
    print(dict(zip(headers, values)))

#table_rows = table.find_all('tr')

#json_body = [
#    {
#        "measurement": "departure",
#        "tags": {
#            "airport": "bsl"
#            },
#        "time": datetime.datetime.now().isoformat(),
#        "fields": {
#            "Float_value": 0.64,
#            "Int_value": 3,
#            "String_value": "Text",
#            "Bool_value": True
#        }
#    }
#]

#departuresListRaw = []
#departuresList = []

#for tr in table_rows:
#    td = tr.find_all('td')
#    row = [i.text for i in td]
#    departuresListRaw.append(row)

timeregex = re.compile('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')

#departuresListRaw = filter(None, departuresListRaw)

#for row in departuresListRaw:
#    print(row[0])
#    if re.search(timeregex, row[1]):
#        departuresList.append()

#for s in departuresListRaw:
#    print(*s)


#if cell.text[:2].isnumeric() = True

#df = pd.read_html(str(table))

#with open('/home/stefan/bsl/departures.html', 'w' ) as f:
# print( tabulate(df[0], headers='keys', tablefmt='html'),file=f )

#df_departures, = pd.read_html('/home/stefan/bsl/departures.html',header=0)
#with open('/home/stefan/bsl/departures.json', 'w' ) as f:
# print(df_departures.to_json(orient='table'),file=f)

#client = InfluxDBClient(host='localhost', port=8086)
#client.switch_database('bsl')

#client.write_points(df_departures.to_json(orient='records'))
