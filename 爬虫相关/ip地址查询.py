import requests
url = 'http://ip.tool.chinaz.com/'
try:
    r = requests.get(url+'183.147.9.220')
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[18570:18700])
except:
    print('爬取失败')
