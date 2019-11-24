import requests
import uuid
import json
from threading import Thread
def get_beauty_info(page):
    key = "93f189f2263647f3ac135d46505bf53b"
    resp = requests.get(
        url=f"http://api.tianapi.com/meinv/index?key={key}&num=10&page={page}")
    data = json.loads(resp.text)
    for beauty in data["newslist"]:
        url = beauty["picUrl"]
        Thread(target=download_picture,args=(url,)).start()
def download_picture(url):
    print(f'正在下载{url}')
    filename = uuid.uuid1().hex + '.jpg'
    resp = requests.get(url)
    with open(f'beauty/{filename}','wb') as file:
        file.write(resp.content)

for page in range(3,5):
    print(f"正在下载第{page}页照片")
    get_beauty_info(page)