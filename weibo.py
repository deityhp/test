# -*- coding: utf-8 -*-
# from bs4 import BeautifulSoup
# import requests
#
# url ='https://s.weibo.com/weibo/%23%E5%A5%A5%E6%96%AF%E5%8D%A1%23?topnav=1&wvr=6&topsug=1'
# w_data = requests.get(url)
# soup = BeautifulSoup(w_data.text,'lxml')
# data = soup.select('div.total > span')
# print(data[1].get_text())


from selenium import webdriver
import time
import re

url ='https://s.weibo.com/weibo/%23%E5%A5%A5%E6%96%AF%E5%8D%A1%23?topnav=1&wvr=6&topsug=1'
def open_web():
    drive = webdriver.Chrome(executable_path= './chromedriver')
    drive.start_client()
    return (drive)
def find_inf():
    info = drive.find_element_by_css_selector('div.total > span:nth-child(2)')
    return info

drive = open_web()
drive.get(url)
time.sleep(3)
info = find_inf().text
str_info = re.findall(r'\d+\.?\d*',info)
print(float(str_info[0]))
drive.close(）