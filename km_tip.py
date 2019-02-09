from bs4 import BeautifulSoup 
from wxpy import *
import requests 
import os
 import time  
url = 'http://195.87.2.30/list_27.xhtml'
 headers = { 
    'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E)', 
    'Cookie':'MYSAPSSO2=AjExMDAgAA5wb3J0YWw6aHVwZW5nMogAE2Jhc2ljYXV0aGVudGljYXRpb24BAAdIVVBFTkcyAgADMDAwAwADRVBQBAAMMjAxODEwMzEwNjA2BQAEAAAADAoAB0hVUEVORzL%2FAPgwgfUGCSqGSIb3DQEHAqCB5zCB5AIBATELMAkGBSsOAwIaBQAwCwYJKoZIhvcNAQcBMYHEMIHBAgEBMBYwDjEMMAoGA1UEAxMDRVBQAgRJ8qc9MAkGBSsOAwIaBQCgXTAYBgkqhkiG9w0BCQMxCwYJKoZIhvcNAQcBMBwGCSqGSIb3DQEJBTEPFw0xODEwMzEwNjA2MzBaMCMGCSqGSIb3DQEJBDEWBBRfThgpLhby3fFgxhOvnH5aiiys3zAJBgcqhkjOOAQDBC8wLQIVAJKQ23pqcX9gwVFAxM%2F8d3usRGF4AhRvhlgEnuDpt92O2%2FHNvjme6EjUGg%3D%3D; SOAMCOOKIE=Fr7LY8YC8HYOQCVznVNJGusj7/AUS5+gXz27d2AEeqy6n0G+yaexq+qNJbiHVxXiuPs3vibRUi3Fb5zaj02E2pS7M3M36sWGHJJi/EoqqBdfThQFblo6m2WHP43TN4FDdhus4tABQv0CCLphdRCeVJDIRyq1dkvsFEJMor2BGgM=; MSHRAP-8000-PORTAL-PSJSESSIONID=zk2wbXvGz5gDs1ydLkvQ6VgL2LMbZCcC!-432031771; ExpirePage=http://cmbchr.cmbc.com.cn:8080/psc/hrsys/; PS_LOGINLIST=http://cmbchr.cmbc.com.cn:8080/hrsys; PS_TOKENEXPIRE=30_Oct_2018_05:45:21_GMT; PS_TOKEN=pwAAAAQDAgEBAAAAvAIAAAAAAAAsAAAABABTaGRyAk4Abwg4AC4AMQAwABRoNxfLgfAVMKJyD55lE3ANVfs0HGcAAAAFAFNkYXRhW3icHco7DkBQEEbh4xGlnbgZ1yNWIEpBpVEJFRq7szh/7hTf5EzmBtIkjiLtLyZMfvLysHNx4MlWBmbyUfQsbMqJ2mOUdBTSZBX0KketcmqTXj+tLkYDP9R5DHY=; SignOnDefault=hupeng2; loginName=hupeng2; KMSSOTokien=FF05FE050BEDEAAB5F7A9ABC3D9E1C33; JSESSIONID=C40F462810033517333DF7EBB2C208FA',
 } 
#获取文件大小 
def get_FileSize(filePath): 
    filePath = filePath 
    fsize = os.path.getsize(filePath) 
    fsize = fsize/float(1024) 
    return round(fsize,2)
   #初始化机器人，扫码登陆 
def act_bot(groupname): 
    bot = Bot(cache_path = True) 
    # 搜索名称含有 groupname的群组
    my_group = bot.groups().search(groupname)[0] 
    return my_group  
#获取网页数据 
def get_web(url,data=None): 
    web_data = requests.get(url, headers = headers) 
    soup = BeautifulSoup(web_data.text, 'lxml') 
    titles = soup.select('a[target="_top"]') 
    data = [] 
    for title in titles: 
        data.append([title.get('title'),title.get('href')]) 
    return data  
#下载文件 
def download_file(href,fname): 
    r = requests.get(href)  # create HTTP response object 
    with open('e:/pdf/2019/' + fname, 'wb') as f: 
        f.write(r.content) 
    print(time.asctime(time.localtime(time.time()))+"成功下载"+fname)
  #发送文件
 def send_file(filehref,filename): 
    my_group = act_bot("玉溪支行主要负责人") 
    my_group1 = act_bot("国务院办公厅") 
    if get_FileSize(filehref) > 500: 
        my_group.send("因" + filename + "文件过大，请到分行OA查看") 
    else: 
    try: 
        my_group.send_file(filehref) 
        my_group1.send_file(filehref) 
        print(time.asctime(time.localtime(time.time()))+"成功发送文件" + filename) 
    except: 
        print(time.asctime(time.localtime(time.time()))+"发送文件失败")
  #睡眠时间判定 
def sleep_time(): 
hour = time.localtime().tm_hour 
if hour > 22: 
    time.sleep(36000) 
else: 
    time.sleep(900)  

while True: 
    #判断网络状态 
    network = 1 
    while network: 
        try: 
            network = 0 
            data = get_web(url) 
        except: 
            network = 1 
            print(time.asctime(time.localtime(time.time()))+"网络异常") 
            time.sleep(600) 
    #判断文件是否曾经发送 
    file = 1 
    i = 0 
    while file: 
        filename = data[i][0] + '.' + (data[i][1])[-3:]  # 获取文件名 
        webhref = 'http://195.87.2.30' + data[i][1]  # 获取下载路径 
        savehref = 'e:/pdf/2019/' + filename  # 设置本地存储路径 
        if os.path.exists(savehref): 
            print(time.asctime(time.localtime(time.time()))+"无新文件") 
            file = 0 
            sleep_time() 
        else: 
            download_file(webhref,filename) #下载文件 
            send_file(savehref, filename) 
            i = i+1    
