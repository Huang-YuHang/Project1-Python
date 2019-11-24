import requests
import json
key = "93f189f2263647f3ac135d46505bf53b"
resp = requests.get(url= f"http://api.tianapi.com/bulletin/index?key={key}")

data = json.loads(resp.text)
for news in data['newslist']:
    print(news['title'])