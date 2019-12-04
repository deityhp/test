#下载民生亿度试题使用
from bs4 import BeautifulSoup
import requests
url = "https://nexam.cmbc.com.cn/wis18/userpaper.viewuserhispaperqueslist.flow"
#需要更改变量
cookie = 'SESSION_CLIENT_DEVICE_KEY=e4e16518-59d0-4a1d-868c-73f6e09815bd; JSESSIONID=gj_P8RBN8bP3t2ywmC7vzITnBaZnLq4XxPr7vIQewTieCfMsjW6k!1426389675; BIGipServerMOEDU_zaixiankaoshixitong_app_7080_pool=!/ivgagJrtBAIw8TE+DPp2e8pdv2HlSo2P7p1wk+CbiATIXGdQd0cjRy/hrZouhBAM4mhNb7xPpatNA=='
p_id = '6286099897724567'
filename = ''

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Cookie':cookie}
txtlist = []
a = 1
for z in range(1,7):
    print(z)

    for i in range(0,300):
        try:
            formdata = {'p_id': p_id,'trys': z,'ques_pos': i}
            web_data = requests.post(url,headers = headers,data=formdata)
            soup = BeautifulSoup(web_data.text,'lxml')
            body = soup.select('tr.STYLE03 > td > div')
            txt = body[0].get_text()
            if txt in txtlist:
                print("试题重复")
            else:
                txtlist.append(txt)
                print(z,i,txt)
                f = open(filename,'a')
                f.write(str(a) +":"+txt+"\n")
                f.close()
                a = a + 1
        except:
            break
