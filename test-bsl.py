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
