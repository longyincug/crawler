import os
import urllib.parse
import requests
import time
from selenium import webdriver
from lxml import etree


class BaiduSpider:
    def __init__(self, url, key):
        keyword = {'word': key}
        self.url = url + urllib.parse.urlencode(keyword)
        self.driver = webdriver.Chrome()
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

    def parse(self):
        selector = etree.HTML(self.driver.page_source)
        content = selector.xpath('//li[@class="imgitem"]/div//img/@data-imgurl')
        return content

    def scroll(self):
        self.driver.maximize_window()
        for i in range(10):
            self.driver.execute_script("document.getElementsByTagName('html')[0].scrollTop=10000")
            time.sleep(1)

    def save(self, content, number):
        with open('images/' + str(number) + '.jpg', 'wb') as f:
            f.write(content)

    def start(self):
        self.driver.get(self.url)
        self.scroll()
        content_list = self.parse()
        try:
            os.mkdir('images')
        except:
            pass
        count = 0
        for each in content_list:
            print(each)
            self.save(requests.get(each, headers=self.headers).content, count)
            count += 1
            print("正在保存第%d张图片" % count)
        self.driver.quit()


if __name__ == "__main__":
    url = "https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fm=result&fr=&sf=1&fmq=1520178299927_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&hs=2&"
    # key = input("请输入关键字：")
    key = '美图'
    baidu = BaiduSpider(url, key)
    baidu.start()
