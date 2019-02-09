# /*-coding = utf-8 -*/
#电影天堂下载电视剧链接提取
import requests
from bs4 import BeautifulSoup

url = 'https://www.xl720.com/thunder/33198.html'
headers = {
    'cookie':'Hm_lvt_c8c350134f0b1e355c0ff58d217bdcb0=1546853173; Hm_lpvt_c8c350134f0b1e355c0ff58d217bdcb0=1546853173; _ga=GA1.2.1812476122.1546853173; _gid=GA1.2.14080381.1546853173',
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

get_db = requests.get(url,headers = headers)
web_db = BeautifulSoup(get_db.text,'lxml')
href = web_db.select('div.ztxt > a')
for href in href:
   print(href.get('href'))

