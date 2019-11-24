import requests
import json
from urllib.parse import quote

TYPER = {
    0 :"可回收垃圾",
    1 :"有害垃圾",
    2:"湿垃圾",
    3:"干垃圾"
}
def search_rubbish(word):
    key =  '93f189f2263647f3ac135d46505bf53b'
    word = quote(word)
    resp = requests.get(url=f"http://api.tianapi.com/txapi/lajifenlei/index?key={key}&word={word}&num=10")
    data = json.loads(resp.text)
    if data['code'] == 200:
        for rubbish in data['newslist']:
            print("垃圾名字:",rubbish['name'])
            print("垃圾属于:",TYPER[rubbish["type"]])
            print("垃圾解释:",rubbish['explain'])
            print("垃圾包含:",rubbish['contain'])
            print("垃圾提示:",rubbish['tip'])
            print("-" * 120)
    else:
        print(data['msg'])


word = input("请输入要搜索的垃圾：")
search_rubbish(word)