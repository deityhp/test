
#下载民生亿度学分信息使用
from bs4 import BeautifulSoup
import time
from selenium import webdriver
url = "https://nedu.cmbc.com.cn/"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
#     'Referer': 'https://nedu.cmbc.com.cn/newcmbcedu/gotoIndexNew?curJsSessionId=lj-SrPTVd8qaf22Tbz0yxslYDJRFI7d8gWKVWZLyq47LE8TW-9PR',
#     'Cookie':'BIGipServerMOEDU_shangxueyuanjiaoxuexitong_app_7080_pool=!sMVFaLg9/YB+oDo850MnSMIxQ8vkDpHA1/YnuAhiQhEg+akRS+Muz9W46A59XKa/FM4tzhjKYNe7FQ==; NEWCMBCEDUJSESSIONID68=lj-SrPTVd8qaf22Tbz0yxslYDJRFI7d8gWKVWZLyq47LE8TW-9PR!894305718'
# }
# re = requests.get(url,headers=headers)
# bs = BeautifulSoup(re.text,'lxml')
# print(bs)
def open_web():
    drive = webdriver.Chrome(executable_path= './chromedriver')
    drive.start_client()
    return (drive)
#打开浏览器，进入民生亿度
driver = open_web()
driver.get(url)
time.sleep(5)
username = driver.find_element_by_id('username')
passsword = driver.find_element_by_id('password')
username.send_keys('hupeng2')
passsword.send_keys('54skycms!')
driver.find_element_by_id('randimages').click()
time.sleep(20)
driver.find_element_by_css_selector('div.login').click()
time.sleep(5)
#进入学习任务，获取未学习信息
driver.find_element_by_xpath('//*[@id="headUL"]/li[2]/a').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="learningtaskfrom"]/div/div/div[2]/ul/li/div[1]/div[3]/span[1]').click()
# lists = driver.find_elements_by_xpath('//*[@id="subtask_resource"]/table/tbody/tr/td/span/a')
lists = driver.find_elements_by_xpath('//*[@id="subtask_resource"]/table/tbody/tr/td')
i = len(lists)
windows = driver.current_window_handle
for li in range(0,i):
    if lists[li].text == "进行中":
        lists[li+3].click()
        driver.switch_to.window(windows)

##进入资源导航，下载课程信息
# driver.find_element_by_xpath('//*[@id="headUL"]/li[4]/a').click()
# time.sleep(3)
# for i in range(1,59):
#     web_data=driver.page_source#    获取网页文件对象
#     soup = BeautifulSoup(web_data,'lxml')
#     names = soup.select('tbody > tr > td:nth-of-type(3) > a')
#     prints = soup.select('tbody > tr > td:nth-of-type(6)')
#     studys = soup.select('tbody > tr > td:nth-of-type(7)')
#     tests = soup.select('tbody > tr > td:nth-of-type(8)')
#     for name,print,study,test in zip(names,prints,studys,tests):
#         w_name = name.get_text()
#         w_print = print.get_text()
#         w_study = study.get_text()
#         w_test = test.get_text()
#         csvfile = open('msedu.csv','a')
#         csvfile.write(w_name + ',' + w_print + ',' + w_study + ',' + w_test + '\n')mayasong-11.txt
#         csvfile.close()
#     driver.find_element_by_css_selector('a.laypage_next').click()