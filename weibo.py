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
# txtpath = r"urls_porn.txt"
# fp = open(txtpath)
# arr = []
# for lines in fp.readlines():
#     lines = lines.strip('\n')
#     arr.append(lines)
# fp.close()
#
# def open_web():
#     drive = webdriver.Chrome(executable_path= './chromedriver')
#     drive.start_client()
#     return (drive)
# def find_inf():
#     info = drive.find_element_by_css_selector('div.total > span:nth-child(2)')
#     return info
#
# drive = open_web()
# for n in arr :
#     name = n[-9:]
#     drive.get(n)
#     drive.save_screenshot('img1/'+name)

# info = find_inf().text
# str_info = re.findall(r'\d+\.?\d*',info)
# print(float(str_info[0]))
# drive.close(）

#支付宝充值
from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
url = 'https://cashierem14.alipay.com/standard/deposit/cashier.htm?orderId=0306cdf68a763aeed924014031NN5888&bizIdentity=pdeposit10001'
def open_web():
    drive = webdriver.Chrome(executable_path= './chromedriver')
    drive.start_client()
    return (drive)
drive = open_web()
drive.get(url)
time.sleep(20)
card = range(861601014982388,861601014982413) #卡号
pwd = range(10)
for i in card:
    now_handle = drive.current_window_handle
    button = drive.find_element_by_css_selector('a[title="充值"]')
    button.click()
    all_handles = drive.window_handles
    drive.switch_to.window(all_handles[-1])
    button = drive.find_elements_by_css_selector('div.ui-fm-item>input[type="submit"]')
    button[1].click()
    select = drive.find_element_by_css_selector('a.ui-select-trigger')
    select.click()
    time.sleep(1)
    value = drive.find_element_by_css_selector('li.ui-select-item[data-value="50"]')
    value.click()
    cardno = drive.find_element_by_css_selector('input#J-cardNo')
    cardno.send_keys(i)
    password = drive.find_element_by_xpath('//*[@id="phoneCardDepositForm"]/fieldset/div[2]/div/table/tbody/tr[1]/td[3]')
    password.click()
    # password.send_keys(pwd[i])
    drive.switch_to.window(now_handle)
