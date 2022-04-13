import requests
from bs4 import BeautifulSoup
import os
import pathlib
import csv

# 路徑
path = pathlib.Path(__file__).parent.absolute()
print(path)

# 建立images資料夾(已經有的話會發生錯誤)
# imagesFile = os.mkdir(f'{path}\images')

# 設定UTF-8-sig 去除\ufeff
file = open(f'{path}\img.csv',encoding='UTF-8-sig')
reader = csv.reader(file)
data = list(reader)
file.close()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}
# 檔名預設值
fileTitle = ''
# 遍歷網址並下載圖片
for d in data:  
    try:
        r = requests.get(d[0], headers = headers)
        soup = BeautifulSoup(r.text, "html.parser")
       
        s = soup.find(class_='rakutenLimitedId_ImageMain1-3')
        img = s.select('img')
        img = img[0]['src'].split('?')[0]
        
        # 取番號作為檔名
        fileTitle = d[0].strip().split('/')
        # 清除回傳串列裡的空字串
        test = [i.strip() for i in fileTitle if i.strip()!='']
        fileTitle = test[-1]
        print(fileTitle)

        # 下載圖片
        f = open(f'{path}\images\{fileTitle}.jpg','wb')
        response = requests.get(img)
        f.write(response.content)
        f.close()
        
    except:
        print(f"{fileTitle} : 下載失敗")