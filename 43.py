from bs4 import BeautifulSoup
import requests
import pymongo
url = "https://bj.xiaozhu.com/"

def save (data):
    client = pymongo.MongoClient('localhost',27017)
    xiaozhu =client['xiaozhu']
    line_data = xiaozhu['line_data']
    line_data.insert_one(data)

def spider (url):
    web_data = requests.get(url)
    soup_data = BeautifulSoup(web_data.text,'lxml')
    titles = soup_data.select('div.result_btm_con.lodgeunitname > div > a > span' )
    prices= soup_data.select('div.result_btm_con > span.result_price')
    for title,price in zip(titles,prices):
        data = {
            "标题":title.get_text(),
            "价格":price.get_text(),
        }
        save(data)
       # print(data)

spider(url)

