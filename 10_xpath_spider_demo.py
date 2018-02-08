# 利用xpath匹配规则爬取指定贴吧内的图片
# 贴吧内每个帖子的链接    //div[@class="threadlist_lz clearfix"]/div/a[@class="j_th_tit "]/@href
# 每个帖子内层主发的图片的链接    //div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src

import urllib.request
import urllib.parse
from lxml import etree
import requests
import re

class ImageSpider():
    def __init__(self, name, start, end):
        """
            根据给定的贴吧名和需要爬取的页码范围，初始化生成一些参数
        """
        self.url = "https://tieba.baidu.com/f"
        self.name = name
        self.start = start
        self.end = end
        # web服务器会针对于不同的浏览器发送不同的页面，所以可能出现xpath helper能匹配，程序却匹配不出的情况，headers尽量用IE标准
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"}

    def load_page(self, pn):
        """
            根据贴吧每页的url，提取出每个帖子链接地址
        """
        #request = urllib.request.Request(url, headers=self.headers)
        #response = urllib.request.urlopen(request)
        #html = response.read()

        kw = {'kw':self.name, 'pn':pn}
        response = requests.get(self.url, params=kw, headers=self.headers)
        html = response.content

        # 利用lxml库的etree模块，将HTML文档解析为HTML DOM模型
        selector = etree.HTML(html)

        # 可以用xpath进行匹配，看清楚class，别忽略空格！
        link_list = selector.xpath('//div[@class="t_con cleafix"]/div/div/div/a[@class="j_th_tit "]/@href')

        print("本页共%d个帖子"%len(link_list))
        count = 1
        for link in link_list:
            full_url = "https://tieba.baidu.com" + link
            self.load_image(full_url, count)
            count += 1

    def load_image(self, url, count):
        """
            根据每个帖子的url，提取出每个层主发的图片链接
        """
        print("---正在下载第%d个帖子的图片---"%count)
        response = requests.get(url, headers=self.headers)
        selector = etree.HTML(response.content)
        img_link_list = selector.xpath('//div[@class="d_post_content j_d_post_content "]/img[@class="BDE_Image"]/@src')
        print("本帖共%d张图片，下载中..."%len(img_link_list))
        for img_link in img_link_list:
            self.write_image(img_link)

    def write_image(self, url):
        """
            根据图片链接，下载保存图片到本地
        """
        response = requests.get(url, headers=self.headers)
        image = response.content
        filename = url[-10:]
        with open('imgs/'+filename, 'wb') as file:
            file.write(image)

    def start_work(self):
        """
            贴吧图片爬取的控制器
        """
        for page in range(self.start, self.end+1):
            pn =  (page-1)*50
            print("-----正在爬取第%d页的帖子内图片-----" % page)
            self.load_page(pn)

if __name__ == "__main__":
    name = input("请输入要爬取图片的贴吧名称: ")
    startPage = int(input("请输入爬取的起始页: "))
    endPage = int(input("请输入爬取的终止页: "))
    spider = ImageSpider(name, startPage, endPage)
    spider.start_work()