import requests
import urllib.request
import json

proxies = {'https': 'https://172.22.42.120:8080'}
proxy = urllib.request.ProxyHandler(proxies)
opener = urllib.request.build_opener(proxy)
urllib.request.install_opener(opener)
url = "https://data-live.flightradar24.com/zones/fcgi/feed.js?faa=1&mlat=1&flarm=1&adsb=1&gnd=1&air=1&vehicles=1&estimated=1&stats=1"
# Get response
response = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
f = urllib.request.urlopen(response)
page = f.read().decode('utf8')
data = json.loads(page)
counter = json.dumps(data, indent=4, sort_keys=True)

#print(len(data))
print(data['full_count'],data['stats']['total']['estimated'])
#print(counter)

