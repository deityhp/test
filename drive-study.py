def open_web():
    drive = webdriver.Chrome(executable_path= './chromedriver')
    drive.start_client()
    return (drive)
def find_inf():
    info = drive.find_element_by_css_selector('div.total > span:nth-child(2)')
    return info

drive = open_web()
for n in arr :
    name = n[-9:]
    drive.get(n)
    drive.save_screenshot('img1/'+name)