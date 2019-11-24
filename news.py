import requests
import json
key = "***"#输入你自己的key
resp = requests.get(url= f"http://api.tianapi.com/bulletin/index?key={key}")

data = json.loads(resp.text)
for news in data['newslist']:
    print(news['title'])
