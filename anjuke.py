
from bs4 import BeautifulSoup
import requests
import random
import time
import csv

#python2可以用file替代open



def spider_2(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    }
    w_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(w_data.text, 'lxml')
    courts = soup.find_all('span',class_='comm-address') #小区
    prices = soup.find_all('span',class_='price-det')#价格
    danjias = soup.find_all('span',class_='unit-price') #单价
    details = soup.find_all('div',class_='house-details')#其他
    titles = soup.find_all('a',class_='houseListTitle')#标题
    hrefs = soup.find_all('a',class_='houseListTitle') # 链接

    for court,price, danjia,detail,title, href in zip(courts,prices,danjias,details,titles, hrefs):
        data = {
            '小区': court.get_text(),
            '总价': price.get_text(),
            '单价': danjia.get_text(),
            '详细': detail.contents[3].get_text(),
            '标题': title.get('title'),
            '链接': href.get('href'),
        }

        # csvfile = open("test.csv", "a")
        # fieldnames = ['小区','总价','单价','详细','标题','链接']
        # writer = csv.DictWriter(csvfile,fieldnames = fieldnames)
        # # 先写入columns_name
        # writer.writerow(data)
        # csvfile.close()
        print(data)


# 循环，把第2-100页全部爬下来
# page = 1
#
# while page < 200 :
#     #url = 'http://esf.km.fang.com/house/i3'+str(page+1)
#     #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
#     url = 'https://km.anjuke.com/sale/d119-o5-p'+str(page+1) +'/?from_price=80&to_price=200&from_area=80&to_area=150'
#     spider_2(url)
#     time.sleep(5)
#     page = page + 1
#     print(page)
url = 'https://km.anjuke.com/prop/view/A1501934352?from=filter&spread=commsearch_p&position=1&kwtype=filter&now_time=1543709456'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
}
def get_xinxi(url):
    wb_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    courts = soup.select('div.houseInfo-content > a')
    adds = soup.select('div.houseInfo-content > p')
    prices = soup.select('span.light.info-tag > em')

    years = soup.select('div.houseInfo-wrap > ul > li:nth-child(7) > div.houseInfo-content')
    titles = soup.select('div.clearfix.title-guarantee > h3')
    print(soup)
    # for court,add,price,danjia,year,title in zip(courts,adds,prices,danjias,years,titles):
    #    data = {
    #        'xiaoqu'：court,
    #        'add': add,
    #        'price': price,
    #        'danjia': danjia,
    #        'year': year,
    #        'title': title,
    #    }
    #    print(data)

get_xinxi(url)










'''
   proxy_list = [
       'http://125.67.73.123',
       'http://202.97.140.147',
       'http://119.29.103.13	',
       'http://121.31.101.217',
       'http://118.178.227.171',
       'http://121.232.145.249',
       'http://117.90.3.59',
       'http://121.31.102.16',
       'http://117.90.0.141',
    ]
    proxy_ip = random.choice(proxy_list) # 随机获取代理ip
    proxies = {'http': proxy_ip}
    headers = {'Host':'www.anjuke.com', 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
    time.sleep(1)
    html = requests.get(url, headers = headers,proxies=proxies)
def spider_2(url):
    headers = {'Host':'www.anjuke.com', 'User-Agent':'Mozilla/5.0 (Windows NT 6.2; rv:16.0) Gecko/20100101 Firefox/16.0'}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    html = opener.open(url)
    soup = BeautifulSoup(html, 'lxml')
    courts =  soup.find_all('span',class_='comm-address') #小区
    prices = soup.find_all('span',class_='price-det')#价格
    danjias = soup.find_all('span',class_='unit-price') #单价
    details = soup.find_all('div',class_='house-details')#其他
    titles = soup.find_all('a',class_='houseListTitle')#标题
    hrefs = soup.find_all('a',class_='houseListTitle') # 链接
    for court,price, danjia,detail,title, href in zip(courts,prices,danjias,details,titles, hrefs):
        data = {
            '小区': court.get_text(),
            '总价': price.get_text(),
            '单价': danjia.get_text(),
            '详细': detail.contents[3].get_text(),
            '标题': title.get('title'),
            '链接': href.get('href'),
        }
        #print(data)
# 循环，把第2-100页全部爬下来
page = 1
while page < 10 :
    url = 'http://esf.km.fang.com/house/i3'+str(page+1)
    #url = 'http://esf.km.fang.com/house/t21-h316-i3'+str(page+1)
    #url = 'https://km.anjuke.com/sale/d119-o5-p'+str(page+1) +'/?from_price=80&to_price=200&from_area=90&to_area=150'
    spider_2(url)
    page = page + 1
 '''
