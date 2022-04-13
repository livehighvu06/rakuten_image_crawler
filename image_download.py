import requests
from bs4 import BeautifulSoup
import os

data = [
    '10002919',
    '10002920',
    '10002921',
    '10002922',
    '10002925',
    '10002926',
    '10003070',
    '10003105',
    '10003110',
    '10003115',
    '10003119',
    '10003121',
    '10003123',
    '10003137',
    '10003139',
    '10003153',
    '10003154',
    '10003156',
    '10003163',
    '10003166',
    '10003167',
    '10003169',
    '10003176',
    '10003178',
    '10003228',
    '10003233',
    '10003238',
    '10003240',
    '10003242',
    '10003245',
    '10003258',
    '10003259',
    '10003260',
    '10003261',
    '10003278',
    '10003322',
    '10003324',
    '10003341',
    '10003342',
    '10003343',
    '10003344',
    '10003345',
    '10003349',
    '10003359',
    '10003360',
    '10003362',
    '10003363',
    '10003365',
    '11313641',
    '11313642',
    '10003064',
    '10003067',
    '10003068',
    '10003069',
    '10002993',
    '10002996',
    '10002998',
    '10003002',
    '10003004',
    '10003008',
    '10003485',
    '10003488',
    '10003491',
    '10003492',
    '10003495',
    '10003497',
    '10003503',
    '10003505',
    '10003507',
    '10003508',
    '10003509',
    '10003512',
    '10003517',
    '10003520',
    '10003522',
    '10003524',
    '10003526',
    '10003528',
    '10003555',
    '10003556',
    '10003557',
    '10003559',
    '10003561',
    '10003563',
    '10003564',
    '10003565',
    '10003566',
    '10003568',
    '10003569',
    '10003571',
    '10003572',
    '10003574',
    '10003576',
    '10003577',
    '10003579',
    '10003580',
    '10003581',
    '10003583',
    '10003544',
    '10003545',
    '10003546',
    '10003548',
    '10003549',
    '10003551',
    '10003552',
    '10003553',
    '10003554',
    '10003620',
    '10003623',
    '10003624',
    '10003625',
    '10003626',
    '10003627',
    '10003628',
    '10003629',
    '10003631',
    '10003633',
    '10003635',
    '10003637',
    '10003639',
    '10003641',
    '10003642',
    '10003646',
    '10003648',
    '10003650',
    '10003653',
    '10003654',
    '10003655',
    '10003656',
    '10003657',
    '10003658',
    '10003659',
    '10003661',
    '10003662',
    '10003663',
    '10003664',
    '10003665',
    '10003666',
    '10003667',
    '10003668',
    '10003669',
    '10003670',
    '10003671',
    '10003672',
    '10003673',
    '10003674'
]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

index = 1

for d in data:  
    try:
        r = requests.get(f'https://item.rakuten.co.jp/athlete-med/{d}', headers = headers)

        soup = BeautifulSoup(r.text, "html.parser")

        s = soup.find(class_='rakutenLimitedId_ImageMain1-3')
        img = s.select('img')
        img = img[0]['src'].replace('?downsize=300:*','')

        print(img)
        
        # 下載圖片
        f = open(f'{d}.jpg','wb')
        response = requests.get(img)
        f.write(response.content)
        f.close()

        print(f"第{index}筆資料 - {d} : 下載成功")
    except:
        print(f"第{index}筆資料 - {d} : 下載失敗")

    index+=1