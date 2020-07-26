# 爬亚马逊
import requests


def getHTMLText(url):
    try:
        # 更改头部信息
        kv = {'user-agent': 'Mozilla/5.0'}
        r = requests.get(url, headers=kv, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text[1000:2000]
    except:
        return '产生异常'


if __name__ == '__main__':
    url = 'https://www.amazon.cn/dp/B0786QNSBD'
    print(getHTMLText(url))
