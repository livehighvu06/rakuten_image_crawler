import requests
from bs4 import BeautifulSoup
import os

data = [
    'ed-s1000mk2',
    'ed-r1380db-br',
    'pca-uvc4kl',
    'uag-aw41cs-',
    'uag-aw45cs-',
    'uag-uawld-',
    'uag-uawsd-',
    'PTFBFH-22W',
    'UAG-IPDPROLS5MK-BK',
    'UP-GSB-A',
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}

index = 1
for d in data:  
    try:
        r = requests.get(f'https://paypaymall.yahoo.co.jp/store/princetondirect/item/{d}', headers = headers)
        # print(r)
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup)
        s = soup.find(class_='ItemImage')
        # print(s)
        img = s.select('amp-img')
        # print(img)
        img = img[0]['src']
        print(img)
       
        # 下載圖片
        # f = open(f'{d}.jpg','wb')
        # response = requests.get(img)
        # f.write(response.content)
        # f.close()
        # print(f"第{index}筆資料 - {d} : 下載成功")
    except:
        print(f"第{index}筆資料 - {d} : 下載失敗")
    
    index+=1