import requests
from pymongo import MongoClient
import time
client = MongoClient('127.0.0.1', 27017)
db = client.lagou
tb = db.fyi

url = 'https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false&isSchoolJob=0'
headers = {
    'Cookie':'user_trace_token=20171202203752-9d4116ad-d75d-11e7-bccf-525400f775ce; LGUID=20171202203752-9d411c9b-d75d-11e7-bccf-525400f775ce; index_location_city=%E5%8C%97%E4%BA%AC; _ga=GA1.2.1482434536.1512218273; JSESSIONID=ABAAABAAAGGABCB3C5F9DC7753FC14B6DF653C57C3A7DF0; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1512218273,1512812792,1513866505; _gid=GA1.2.1178766657.1513866505; TG-TRACK-CODE=index_search; LGSID=20171221231527-c67416d9-e661-11e7-9dff-5254005c3644; PRE_UTM=; PRE_HOST=; PRE_SITE=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist_%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2F; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1513870422; _gat=1; LGRID=20171221233341-52d9c982-e664-11e7-a450-525400f775ce; SEARCH_ID=5f049d18b9f04683bf059d8940cb32e2',
    'Referer':'https://www.lagou.com/jobs/list_web%E5%89%8D%E7%AB%AF?labelWords=sug&fromSearch=true&suginput=web',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'
}

def Get_Data(page, keys):
    for i in range(page):
        payload = {
            'first':'true',
            'pn':i,
            'kd':keys
        }
        request = requests.post(url, data=payload, headers=headers)
        tb.insert(request.json()['content']['positionResult']['result'])
        print('正在爬取第%s页'%str(i+1))
        time.sleep(3)

if __name__ == '__main__':
    keys = input('请输入搜索关键字：')
    Get_Data(31, keys)