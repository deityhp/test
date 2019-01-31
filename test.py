j98mj98j9
# https://api.yii.dgtle.com/v2/index?token=&perpage=14&page=7&dateline=1540544640
# https://api.yii.dgtle.com/v2/index?token=&perpage=14&page=8&dateline=1540472471
# https://api.yii.dgtle.com/v2/index?token=&perpage=14&page=9&dateline=1540429860
from bs4 import BeautifulSoup
import  requests
import  time
import re
url = 'http://www.dgtle.com/portal.php?mod=index&ajaxlist=1&mobile=yes&page='
headers = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
    'Cookie': 'discuz_804f_saltkey=T361Jj3J; discuz_804f_lastvisit=1541049271; pgv_pvi=5176926796; pgv_info=ssi=s1267979890; UM_distinctid=166cde8da5c30a-0d888d0f976fb6-1e396652-232800-166cde8da5fcea; CNZZDATA1258616523=1221413854-1541049552-https%253A%252F%252Fwww.google.com%252F%7C1541054956; discuz_804f_paging_time=1541055683; discuz_804f_pvi=1543499308; discuz_804f_si=s1714016704; discuz_804f_pc_size_c=0; CNZZDATA1255971922=85125340-1541051984-null%7C1541051984; Hm_lvt_67ec8eb5072484bbaa9834e17e871c0b=1541055681; Hm_lpvt_67ec8eb5072484bbaa9834e17e871c0b=1541055681; discuz_804f_lastact=1541055698%09portal.php%09index',
}
def get_url(url,data=None):
    w_data = requests.get(url,headers = headers)
    soup = BeautifulSoup(w_data.text,'lxml')
    titles = soup.select('dt.zjj_title > a')
    img = soup.select('dd.m > a')
    ty = soup.select(' div.portallist_cat')


    for title,img,ty in zip(titles,img,ty):
        data = {
            'title':title.get_text(),
            'img': re.findall('\((.*?)\)', img.get('style')),
            'ty':ty.get_text(),
        }
        print(data)
def get_more_page(start,end):
    for one in range(start,end):
        get_url(url + str(one))
        time.sleep(3)
get_more_page(1,10)
