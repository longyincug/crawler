from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.PhantomJS()

driver.get('http://www.douban.com/')

driver.save_screenshot('douban.png')
