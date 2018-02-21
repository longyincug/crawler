from selenium import webdriver
import unittest
from lxml import etree
import time

class DouYu():
    def __init__(self):
        self.driver = webdriver.PhantomJS()
    
    def testDouyu(self):
        self.driver.get('https://www.douyu.com/directory/all')
        count = 0
        while True:
            selector = etree.HTML(self.driver.page_source)
            names = selector.xpath('//span[@class="dy-num fr"]/preceding-sibling::span[1]')
            numbers = selector.xpath('//span[@class="dy-num fr"]')
            for name,number in zip(names, numbers):
                print('直播间人数：%s，\t主播名：%s'%(number.text.strip(), name.text.strip()))
            count += 1
            print('-----以上为第%d页-----'%count)
            if self.driver.page_source.find('shark-pager-disable-next') != -1:
                break
            self.driver.find_element_by_class_name('shark-pager-next').click()
            time.sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    douyu = DouYu()
    douyu.testDouyu()
    douyu.tearDown()

            
