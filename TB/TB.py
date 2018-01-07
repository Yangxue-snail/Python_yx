from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
import re
import urllib.request
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
tb = client.taobao
db = tb.taobao3_python
browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)

def search(Keys):
    try:
        browser.get('http://www.taobao.com')
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#q')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_TSearchForm>div.search-button>button')))
        input.send_keys(Keys)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager>div>div>div>div.total')))
        get_product()
        return total.text
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager>div>div>div>div.form>input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager>div>div>div>div.form>span.btn.J_Submit')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager>div>div>div>ul>li.item.active>span'), str(page_number)))
        get_product()
    except TimeoutException:
        next_page(page_number)

def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    count = 0
    for item in items:
        count+=1
        products = {
            # 'image': item.find('.pic .img').attr('src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text()[:-3],
            'title':item.find('.title').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text(),
            # 'pic':item.find('.J_ItemPic.img').attr('src')
        }
        a = item.find('.J_ItemPic.img')
        if a.attr('src'):
            products['src'] = 'http:'+ a.attr('src')
        else:
            products['src']= 'http:'+ a.attr('data-ks-lazyload')
        print(products)
        response  = urllib.request.urlopen(products['src'])
        img = response.read()
        with open(str(count)+'.jpg', 'wb') as f:
            f.write(img)

        db.insert(products)



def main():
    Keys = input('请输入搜索关键字：')
    total = search(Keys)
    total = int(re.compile('(\d+)').search(total).group(1))
    for i in range(2, 11):
        next_page(i)

if __name__ == '__main__':
    main()