from bs4 import BeautifulSoup
import requests
url = "https://nexam.cmbc.com.cn/wis18/userpaper.viewuserhispaperqueslist.flow"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Cookie':'SESSION_CLIENT_DEVICE_KEY=96381dd1-07fc-4af2-a4d2-6423ac661b61; BIGipServerMOEDU_zaixiankaoshixitong_app_7080_pool=323039528.43035.0000; JSESSIONID=1OWD9BdaY0T4IiONhjflJZD5WudDAIjWBLd8_gCEi2-rJmVi0vGn!-1029881665',
}
for i in range(0,290):
    formdata = {'p_id': '6045754856578267','trys': '1','ques_pos': i}
    web_data = requests.post(url,headers = headers,data=formdata)
    soup = BeautifulSoup(web_data.text,'lxml')
    body = soup.select('tr.STYLE03 > td > div')
    txt = body[0].get_text()
    print(txt)
    f = open('test1.txt','a')
    f.write(str(i) +":"+txt+"\n")
    f.close()
