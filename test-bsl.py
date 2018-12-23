import urllib.request
from html_table_parser import HTMLTableParser

target = 'https://www.euroairport.com/en/passengers-visitors/arrivals-departures/flights/departures.html'

# get website content
req = urllib.request.Request(url=target)
f = urllib.request.urlopen(req)
xhtml = f.read().decode('utf-8')

# instantiate the parser and feed it
p = HTMLTableParser()
p.feed(xhtml)
print(p.tables)


departuresListRaw = []
departuresListRaw = p.tables
departuresListRaw = filter(None, departuresListRaw)
departuresList = []

timeregex = re.compile('^([0-9]|0[0-9]|1[0-9]|2[0-3]):[0-5][0-9]$')


for row in departuresListRaw:
    print(row[0])
    if re.search(timeregex, row[1]):
        departuresList.append()

for s in departuresList:
    print(*s)
