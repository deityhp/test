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
#自动学习
def auto_study():
    list_windows = []
    list_len = len(driver.find_elements_by_xpath('//*[@id="subtask_resource"]/table/tbody/tr/td[3]')) +1
    for li in range(1,list_len):
        list_xpath1 = '//*[@id="subtask_resource"]/table/tbody/tr['+str(li*2)+']/td[3]'
        list_xpath2 = '//*[@id="subtask_resource"]/table/tbody/tr['+str(li*2)+']/td[6]/span/a'
        if driver.find_element_by_xpath(list_xpath1).text != '已完成':
            list_butt = driver.find_elements_by_xpath(list_xpath2)
            for list in list_butt:
                if list.text == "学习":
                    list.click()
                    all_handles = driver.window_handles
                    driver.switch_to.window(all_handles[-1])
                    try:
                        driver.find_element_by_css_selector('div.main1 > div > a.orangebtn').click()
                    except:
                        driver.close()
                        driver.switch_to.window(windows)
                        print("此门课程无法学习")
                    time.sleep(2)
                    titles = driver.find_elements_by_xpath('//*[@id="contentList"]/div/div/div/div[2]/div[2]/table/tbody/tr/td[2]/div')
                    i = len(titles) + 1
                    print('此课程共有' + str(i) + '项学习内容')
                    windows_stu = driver.current_window_handle
                    x =0
                    for tit in range(1,i):
                        print('现在开始学习第'+ str(tit)+'项')
                        xpath1 = '//*[@id="contentList"]/div/div/div/div[2]/div[2]/table/tbody/tr['+str(tit)+']/td[2]/div'
                        xpath2 = '//*[@id="contentList"]/div/div/div/div[2]/div[2]/table/tbody/tr['+str(tit)+']/td[8]/div/a[1]'
                        if driver.find_element_by_xpath(xpath1).text == '否':
                            driver.find_element_by_xpath(xpath2).click()
                            all_handles = driver.window_handles
                            list_windows.append(all_handles[-1])
                            driver.switch_to.window(windows_stu)
                            x = x+1
                        if (tit == i-1) and (x == 0):
                            driver.close()
                            print('此课程已学习')
                            break
                driver.switch_to.window(windows)
            break
    print(str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))+"已打开所有需学习窗口，等待15分钟")
    time.sleep(60)
    print('请关闭学习窗口后输入Y')
    # #关闭打开的学习窗口
    # for window in list_windows:
    #     driver.switch_to.window(window)
    #     time.sleep(0.5)
    #     driver.close()
    #     time.sleep(0.5)
    input()
    print('课程学习已完成')
#点击所有评估按钮
def click_answer():
    lists_assess = driver.find_elements_by_xpath('//*[@id="subtask_resource"]/table/tbody/tr/td[6]/span/a')
    driver.switch_to.window(windows)
    for li in lists_assess:
        try:
            if li.text =='评估':
                li.click()
                time.sleep(0.5)
                list_star =driver.find_elements_by_css_selector('img[title="5"]')
                for stat in list_star:
                    stat.click()
                    time.sleep(0.5)
                answer = driver.find_element_by_css_selector('textarea')
                answer.send_keys('无')
                driver.find_element_by_id('btnCommit').click()
                time.sleep(0.5)
                driver.find_element_by_css_selector('a.layui-layer-btn0').click()
        except:
            time.sleep(0.5)
            driver.find_element_by_css_selector('a.layui-layer-btn0').click()
            print('本门课程未完成学习')
    print("已完成所有课程评估")
#选择学习课程
def select_point(p):
    driver.find_element_by_xpath('//*[@id="headUL"]/li[4]/a').click()
    time.sleep(3)
    #选择分值1分以上，无需考试的课程
    points =0
    for i in range(1,70):
        for no in range(2,21):
            list_xpath1 = '//*[@id="onlineCourseList"]/div[1]/div[4]/div[2]/div/table/tbody/tr['+str(no)+']/td[6]'
            list_xpath2 = '//*[@id="onlineCourseList"]/div[1]/div[4]/div[2]/div/table/tbody/tr[' + str(no) + ']/td[8]'
            list_xpath3 = '//*[@id="onlineCourseList"]/div[1]/div[4]/div[2]/div/table/tbody/tr[' + str(no) + ']/td[9]'
            list_xpath4 = '//*[@id="onlineCourseList"]/div[1]/div[4]/div[2]/div/table/tbody/tr[' + str(no) + ']/td[1]'
            point = float(driver.find_element_by_xpath(list_xpath1).text)
            test = driver.find_element_by_xpath(list_xpath2).text
            info = driver.find_element_by_xpath(list_xpath3).text
            if point>=1 and test == "-/-" and info == "未获得学分":
                driver.find_element_by_xpath(list_xpath4).click()
                driver.find_element_by_xpath('//*[@id="course-electivecourse"]').click()
                time.sleep(2)
                driver.find_element_by_css_selector('div.mian_modal > div > div.mian_modal_button').click()
                points = points + point
        print("本次已选择" + str(points) +"分")
        #划定学分上限
        if points >= p :
            break
        driver.find_element_by_css_selector('a.laypage_next').click()
#主程序开始
def main():
    #打开浏览器，进入民生亿度
    print("请输入要选增的学分")
    point = float(input())
    print("请输入民生亿度用户名")
    un = input()
    print("请输入民生亿度密码")
    pw = input()
    driver = open_web()
    driver.get(url)
    time.sleep(2)
    username = driver.find_element_by_id('username')
    passsword = driver.find_element_by_id('password')
    randnum = driver.find_element_by_id('validateCode')
    username.send_keys(un)
    passsword.send_keys(pw)
    driver.find_element_by_id('randimages').click()
    time.sleep(1)
    driver.find_element_by_css_selector('#layui-layer1 > div.layui-layer-btn > a').click()
    print("请输入验证码")
    rand = input()
    randnum.send_keys(rand)
    driver.find_element_by_css_selector('div.login').click()
    time.sleep(2)
    #进入学习任务
    driver.find_element_by_xpath('//*[@id="headUL"]/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="learningtaskfrom"]/div/div/div[2]/ul/li/div[1]/div[3]/span[1]').click()
    windows = driver.current_window_handle
    if point > 0 :
        print("现在开始选课")
        select_point(point)
    driver.switch_to.window(windows)
    time.sleep(2)
    print("现在开始学习")
    auto_study()
    driver.switch_to.window(windows)
    driver.find_element_by_xpath('//*[@id="headUL"]/li[2]/a').click()
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="learningtaskfrom"]/div/div/div[2]/ul/li/div[1]/div[3]/span[1]').click()
    time.sleep(2)
    print("现在开始评估")
    click_answer()
if __name__ == '__main__':
    main()


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