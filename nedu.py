from bs4 import BeautifulSoup
import requests
url = "https://nexam.cmbc.com.cn/wis18/userpaper.viewuserhispaperqueslist.flow"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36',
    'Cookie':'SESSION_CLIENT_DEVICE_KEY=e4e16518-59d0-4a1d-868c-73f6e09815bd; JSESSIONID=d1jmVpCGEvhYsoeXtFhZPbWB5dzyB7kzUeWRCNAzx33TfElVJ6Lw!449643258; BIGipServerMOEDU_zaixiankaoshixitong_app_7080_pool=!HhXf5pNPap4iZiw850MnSMIxQ8vkDjBT6jbjs9XV29chykUPgw0oX5WM+WYXvLPPorSjEZ+JZuLggg=='
}

for z in range(1,5):
    print(z)

    for i in range(0,300):
        try:
            formdata = {'p_id': '6149561832314243','trys': z,'ques_pos': i}
            web_data = requests.post(url,headers = headers,data=formdata)
            soup = BeautifulSoup(web_data.text,'lxml')
            body = soup.select('tr.STYLE03 > td > div')
            txt = body[0].get_text()
            print(txt)
            f = open('liyuansong.txt','a')
            f.write(str(i) +":"+txt+"\n")
            f.close()
        except:
            break
