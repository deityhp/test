from bs4 import BeautifulSoup
from wxpy import *
import requests
import re
import time
url = 'http://195.87.2.30/list_27.xhtml'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)',
    'Cookie':'MYSAPSSO2=AjExMDAgAA5wb3J0YWw6aHVwZW5nMogAE2Jhc2ljYXV0aGVudGljYXRpb24BAAdIVVBFTkcyAgADMDAwAwADRVBQBAAMMjAxODEwMzEwNjA2BQAEAAAADAoAB0hVUEVORzL%2FAPgwgfUGCSqGSIb3DQEHAqCB5zCB5AIBATELMAkGBSsOAwIaBQAwCwYJKoZIhvcNAQcBMYHEMIHBAgEBMBYwDjEMMAoGA1UEAxMDRVBQAgRJ8qc9MAkGBSsOAwIaBQCgXTAYBgkqhkiG9w0BCQMxCwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0xODEwMzEwNjA2MzBaMCMGCSqGSIb3DQEJBDEWBBRfThgpLhby3fFgxhOvnH5aiiys3zAJBgcqhkjOOAQDBC8wLQIVAJKQ23pqcX9gwVFAxM%2F8d3usRGF4AhRvhlgEnuDpt92O2%2FHNvjme6EjUGg%3D%3D; SOAMCOOKIE=Fr7LY8YC8HYOQCVznVNJGusj7/AUS5+gXz27d2AEeqy6n0G+yaexq+qNJbiHVxXiuPs3vibRUi3Fb5zaj02E2pS7M3M36sWGHJJi/EoqqBdfThQFblo6m2WHP43TN4FDdhus4tABQv0CCLphdRCeVJDIRyq1dkvsFEJMor2BGgM=; MSHRAP-8000-PORTAL-PSJSESSIONID=zk2wbXvGz5gDs1ydLkvQ6VgL2LMbZCcC!-432031771; ExpirePage=http://cmbchr.cmbc.com.cn:8080/psc/hrsys/; PS_LOGINLIST=http://cmbchr.cmbc.com.cn:8080/hrsys; PS_TOKENEXPIRE=30_Oct_2018_05:45:21_GMT; PS_TOKEN=pwAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABRoNxfLgfAVMKJyD55lE3ANVfs0HGcAAAAFAFNkYXRhW3icHco7DkBQEEbh4xGlnbgZ1yNWIEpBpVEJFRq7szh/7hTf5EzmBtIkjiLtLyZMfvLysHNx4MlWBmbyUfQsbMqJ2mOUdBTSZBX0KketcmqTXj+tLkYDP9R5DHY=; SignOnDefault=hupeng2; loginName=hupeng2; KMSSOTokien=FF05FE050BEDEAAB5F7A9ABC3D9E1C33; JSESSIONID=C40F462810033517333DF7EBB2C208FA',
}


#初始化机器人，扫码登陆


bot = Bot(cache_path = True)
# 搜索名称含有 "胡鹏" 的男性玉溪好友
my_group = bot.groups().search('国务院办公厅')[0]
send_group = bot.groups().search('玉溪支行主要负责人')[0]

def get_pdf(url,data=None):
    pdf_data = requests.get(url, headers = headers)
    soup = BeautifulSoup(pdf_data.text, 'lxml')
    titles = soup.select('a[target="_top"]')
    data = []
    for title in titles:
       data.append([title.get('title'),title.get('href')])
    return data

w_num = '714'

while True:
    data = get_pdf(url)
    filename = re.findall(r'\d+', data[0][0])

    while filename == []:
       filename = re.findall(r'\d+', data[1][0])
       if filename == []:
           time.sleep(600)
           data = get_pdf(url)
           filename = re.findall(r'\d+', data[0][0])
       else:
           del data[0]



    if w_num == filename[1]:
        #my_friend.send(title)
       # my_friend.send_file('e:/pdf/1.pdf')
        print(time.asctime( time.localtime(time.time()) )+'无新文件')
        # print(str(int(filename[1]) + 1))
        hour = time.localtime().tm_hour
        if hour > 22:
            time.sleep(36000)
        else:
            time.sleep(900)
    else:
        f_num = int(filename[1]) - int(w_num)
        while not f_num == 0:
            filename = re.findall(r'\d+', data[f_num-1][0])

            fname = filename[0] + filename[1]+'.'+ (data[0][1])[-3:]
            href = 'http://195.87.2.30' + data[f_num-1][1]
            r = requests.get(href)  # create HTTP response object
            with open('e:/pdf/' + fname, 'wb') as f:
                f.write(r.content)
                pdf = 'e:/pdf/' + fname
                my_group.send_file(pdf)
                send_group.send_file(pdf)
            print('已发送文件'+fname)
            f_num = f_num - 1
            w_num = re.findall(r'\d+', data[0][0])[1]

