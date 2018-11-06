# https://36kr.com/api/search-column/mainsite?per_page=20&page=2&_=1541402050022
# https://36kr.com/api/search-column/mainsite?per_page=20&page=3&_=1541402079041
# /*-coding = utf-8 -*/
import requests
from bs4 import BeautifulSoup
headers = {
    'Cookie':'device-uid=8b2cd600-a415-11e8-8308-d1588fdd7592; kr_stat_uuid=QfxrQ25578788; download_animation=1; acw_tc=276aede215414020072166288e5ff6601f19b974d0813b88f114f362af234b; krnewsfrontss=5ead22d4d2bbaf982a46fe0fefd1ef66; M-XSRF-TOKEN=de89739e08e70ffacd4ea23e276bb1fbae3a1d2cf818ec3d27882cdf630c5844; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22QfxrQ25578788%22%2C%22%24device_id%22%3A%2216554e043a95db-07cf03d313f044-163b6952-2304000-16554e043aad66%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%2C%22first_id%22%3A%2216554e043a95db-07cf03d313f044-163b6952-2304000-16554e043aad66%22%7D; TY_SESSION_ID=bc56d6f7-0ec6-4300-a1a4-d6a759717a76; Hm_lvt_713123c60a0e86982326bae1a51083e1=1541402010,1541402766; Hm_lpvt_713123c60a0e86982326bae1a51083e1=1541402766; Hm_lvt_1684191ccae0314c6254306a8333d090=1541402010,1541402766; Hm_lpvt_1684191ccae0314c6254306a8333d090=1541402766; identity_id=4500794045104390',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}



url = 'https://36kr.com/api/search-column/mainsite?per_page=20&page=3'
w_data = requests.get(url,headers = headers)
print(w_data.text)

