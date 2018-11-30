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
url ='http://mp.weixin.qq.com/mp/jsreport?1=1&key=2&content=biz:MzA5NTQ0MTEyNw==,mid:2652180661,uin:777[key2]ajax_err&r=0.18012391988602539'
