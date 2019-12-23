#获取网页信息
from bs4 import BeautifulSoup
import requests

url = 'http://www.cpta.com.cn/GB/397553/index.html'
response = requests.get(url)
response.encoding = 'gb2312'
soup = BeautifulSoup(response.text,'lxml')
lists = soup.select('body > div.p2j_bg.clearfix > div > div.fl.left > ul > li > a')
for list in lists:
    print(list.text)