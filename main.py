#coding=utf8
# import  itchat
# itchat.auto_login(hotReload=True)   #热启动你的微信
# #itchat.run()
# rooms=itchat.get_chatrooms(update=True)
# for i in range(len(rooms)):
#     print(rooms[i])   #查看你多有的群
#
# room = itchat.search_friends(name=r'爱宝宝')  #这里输入你好友的名字或备注。
# print(room)
# userName = room[0]['UserName']
# f="./23.py"  #图片地址
# try:
#     itchat.send_file(f,toUserName=userName)  #如果是其他文件可以直接send_file
#     print("success")
# except:
#     print("fail")


from bs4 import BeautifulSoup
import requests
import time
# url = 'https://www.qipamaijia.com/index/'

# def get_img(url):
#     wb_data = requests.get(url)
#     soup = BeautifulSoup(wb_data.text,'lxml')
#     imgs = soup.select( 'div.block > div.thumb > a > img')
#     for img in zip(imgs):
#         src = img[0].get('src')
#         name = src[-9:]
#         save_img(src,name)
#         print(time.asctime( time.localtime(time.time()) )+ name + '保存完成')
#下载小图片
txtpath = r"urls_porn.txt"
fp = open(txtpath)
arr = []
for lines in fp.readlines():
    lines = lines.strip('\n')
    arr.append(lines)
fp.close()


def save_img(src,name):
    html = requests.get(src)
    print(html)
    with open('img2/'+name, 'wb') as file:
        file.write(html.content)
for n in arr:
    print(n)
    name = n[-9:]
    save_img(n,name)
    print("已下载"+name)
