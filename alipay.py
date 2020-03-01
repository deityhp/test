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
