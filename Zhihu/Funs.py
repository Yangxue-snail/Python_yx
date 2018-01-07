import requests
import pandas as pd
import time
headers = {
    'authorization':'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
    'Cache-Control':'no-cache',
    'Referer':'https://www.zhihu.com/people/excited-vczh/followers',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
    'Cookie':'_zap=f2d99e14-0701-4c4f-8630-53f8e74a31dc; d_c0="AGDCC-hYugyPTnOhlmtONkVy0LT3QNDhjss=|1511443985"; __utma=51854390.22415140.1512056927.1512056927.1512056927.1; __utmz=51854390.1512056927.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20150808=1^3=entry_date=20150808=1; q_c1=634dab03159747ba957226ea27a89fe2|1513483454000|1510758556000; aliyungf_tc=AQAAAIisJX2LuQgAnEZ/fCuuLReFCX8d; _xsrf=88b9aecd-001e-485e-b030-ff40bea02521',
    'X-UDID': 'AGDCC-hYugyPTnOhlmtONkVy0LT3QNDhjss='
    'httppost.addHeader( “ZERR_NO_AUTH_TOKEN”,”FTeR0c8arOPKh8c5DYh_9uu98_zJbaWw53J-Sch9MTg”)'

}
user = []
def Get(page):
    for i in range(page):
        url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followers?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
        request = requests.get(url, headers=headers)
        user.extend(request)
        print('正在爬取第%s页'%str(i+1))
        time.sleep(1)
if __name__ == '__main__':
    Get(3)
    print(user)
    # df = pd.DataFrame.from_dict(user)
    # df.to_csv('Funs.csv')


# import  requests
# import  pandas as pd
# from lxml import etree
# import  time
# header = {
#     'authorization':'Bearer 2|1:0|10:1511444021|4:z_c0|92:Mi4xY2pfMUFRQUFBQUFBWU1JTDZGaTZEQ2NBQUFDRUFsVk5OVnMtV2dERG5vT3ZQWFZLdW9za1JIY2RIS0I4R192RmlB|040ea03387b10aa659413c7f1c789415e2ca23e9bd9c77cbf8826d474d6c390d',
#     'Cookie':'_zap=f2d99e14-0701-4c4f-8630-53f8e74a31dc; l_cap_id="ODI1YjczMjk2MTYxNDI1NTg5NjM1NjM0YzYwYTIxYzc=|1511443984|b89d2ce2f06ca8bbd292518cb2db7014429c2c1a"; r_cap_id="Zjg1ZTRmODM1MTRkNGFkOTk2YTExYThjNDVmNmM2M2U=|1511443984|605295c30faca586452776c3e338f47c8e9147f0"; cap_id="ZGFmNjg5OGI3NWUyNGU5NTkxZTg3MWM4NzA2MDBhYTk=|1511443984|4642f507b38d96c0b04d6da2834e4aaa5c022e94"; d_c0="AGDCC-hYugyPTnOhlmtONkVy0LT3QNDhjss=|1511443985"; z_c0="2|1:0|10:1511444021|4:z_c0|92:Mi4xY2pfMUFRQUFBQUFBWU1JTDZGaTZEQ2NBQUFDRUFsVk5OVnMtV2dERG5vT3ZQWFZLdW9za1JIY2RIS0I4R192RmlB|040ea03387b10aa659413c7f1c789415e2ca23e9bd9c77cbf8826d474d6c390d"; __utma=51854390.22415140.1512056927.1512056927.1512056927.1; __utmz=51854390.1512056927.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20150808=1^3=entry_date=20150808=1; aliyungf_tc=AQAAAB2MMhPozgoAnEZ/fO+sF9n1KSBP; q_c1=634dab03159747ba957226ea27a89fe2|1513483454000|1510758556000; _xsrf=7526d1b9-e373-4dbb-b531-d1b1d415003c',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
# }
# user_data = []
# def get_user_data(page):
#     for i in range(page):
#         url = 'https://www.zhihu.com/api/v4/members/excited-vczh/followees?include=data%5B*%5D.answer_count%2Carticles_count%2Cgender%2Cfollower_count%2Cis_followed%2Cis_following%2Cbadge%5B%3F(type%3Dbest_answerer)%5D.topics&offset={}&limit=20'.format(i*20)
#         r = requests.get(url, headers=header).json()['data']
#         user_data.extend(r)
#         print('正在爬取第%s页'%str(i+1))
#         time.sleep(1)
# if __name__ == '__main__':
#     get_user_data(5)
#     df = pd.DataFrame.from_dict(user_data)
#     df.to_csv('zh.csv')
