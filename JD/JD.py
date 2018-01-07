from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from pyquery import PyQuery as pq
from selenium.common.exceptions import TimeoutException
import time
import urllib.request
from pymongo import MongoClient
client = MongoClient('127.0.0.1', 27017)
tb = client.JD
db = tb.iphonex
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)

def search(Keys):
    try:
        browser.get('https://www.jd.com/')
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#key')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#search>div.search-m>div.form>button')))
        input.clear()
        input.send_keys(Keys)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage>span.p-skip>em>b')))

        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(3)

        get_products()
        return total
    except TimeoutException:
        return search()

def next_page(page_number):
    try:
        input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage>span.p-skip>input')))
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#J_bottomPage>span.p-skip>a')))
        input.clear()
        input.send_keys(page_number)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage>span.p-num>a.curr'), str(page_number)))

        js = "var q=document.documentElement.scrollTop=100000"
        browser.execute_script(js)
        time.sleep(3)

        get_products()
    except TimeoutException:
        next_page(page_number)



def get_products():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList>ul.gl-warp.clearfix')))
    html = browser.page_source
    doc =pq(html)
    items = doc('#J_goodsList .gl-warp.clearfix .gl-item').items()
    count = 0
    for item in items:
        count+=1
        products={
            'title':item.find('.p-name.p-name-type-2').text(),
            'info':item.find('.p-commit').text()[:-3],
            'shop':item.find('.J_im_icon').text(),
            'price':item.find('.p-price').text(),
            # 'src':item.find('.err-product').attr('data-lazy-img')
        }
        a = item.find('.err-product')
        if (a.attr('src')):
            # print(a.attr('src'))

            products['src'] = 'http:' + a.attr('src')
        else:
            # print(a.attr("data-lazy-img")) 懒加载前src没有值用data-lazy-img，当屏幕滚动触发图片懒加载将data-lazy-img值赋给src，所以这里有个判断
            products['src'] = 'http:' + a.attr('data-lazy-img')
        print(products)
        db.insert(products)
        response  = urllib.request.urlopen(products['src'])
        img = response.read()
        with open('iphonex'+str(count)+'.jpg', 'wb') as f:
            f.write(img)
def main():
    Keys = input('请输入搜索的关键字：')
    total = search(Keys)
    for i in range(2, 21):
        next_page(i)
if __name__ == '__main__':

    main()


