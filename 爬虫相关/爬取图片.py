import requests
import os
url = 'https://i0.hdslb.com/bfs/album/608c7e17502d88205b5c46cdd1704d7694eb7788.jpg@518w_1e_1c.jpg'
root = 'D://pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, 'wb') as f:
            f.write(r.content)
            f.close()
            print('文件保存成功')
    else:
        print('文件已存在')
except Exception:
    print('爬取失败')
