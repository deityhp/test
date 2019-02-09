from selenium import webdriver

browser = webdriver.Chrome()
url = "http://www.21wecan.com/rcpj/ksrk/wsbmzq/"
browser.set_window_size(1200, 900)
browser.get(url)

browser.save_screenshot("codingpy.png")
browser.close()