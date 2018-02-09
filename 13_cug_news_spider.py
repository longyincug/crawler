import requests
from lxml import etree
import re
import json

class NewsSpider():

    def __init__(self, url_list):
        self.url_list = url_list

    def start_work(self):
        """
            爬取工作的总调度器
            将给定的新闻栏目的网址一一进行处理
        """
        # 遍历所有给出的新闻栏目
        for each in self.url_list:
            name, url = each

            # 获取该栏目下新闻的总页数
            page_num = self.get_nums(url)

            # 将每一页的url 存到列表里
            full_url_list = self.url_control(url, page_num)

            news_list = []

            # 开始对每一页进行内容爬取
            for url in full_url_list:
                html = self.load_page(url)

                # 生成便于xpath匹配的DOM文档
                selector = etree.HTML(html)

                # 获取匹配到的内容列表
                news_list = self.find_news(selector, name, news_list)

            news_list = [eval(x) for x in news_list]

            # print(len(news_list))

            # 写入json文件到本地
            self.write_news(news_list, name)

    def get_nums(self, url):
        """
            获得某个栏目下新闻的页码总数
        """
        html = self.load_page(url).decode('utf-8')
        # 用正则获取页码总数
        pattern = re.compile('fanye177473.+?1/(\d+).+?</td>', re.I)
        return pattern.search(html).group(1)

    def url_control(self, url, page_num):
        """
            url页码控制
            遍历每个name栏目下所有的页码，组合生成要爬取页面的url
        """
        full_url_list = []
        for i in list(range(1, int(page_num)+1))[::-1]:
            if i == int(page_num):
                i = ''
            else:
                i = '/' + str(i)
            full_url = url[:-4] + i + url[-4:]
            full_url_list.append(full_url)
        return full_url_list

    def load_page(self, url):
        """
            根据给定的url发起请求，拿到html源码
        """
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        response = requests.get(url, headers=headers)
        content = response.content
        return content

    def find_news(self, selector, name, news_list):
        """
            根据给定html源码，从中匹配出新闻的标题、日期和链接
        """
        notices = selector.xpath('//li[@class="list_item"]')
        for each in notices:
            title = each.xpath('./a')[0].text
            link = each.xpath('./a/@href')[0]
            if "http" not in link:
                link = "http://www.cug.edu.cn/" + link.replace("../", '')
            date = each.xpath('./span')[0].text
            data = {'title':title,
                      'link':link,
                      'date':date,
            }
            # 进行除重操作
            data = str(data)
            if data not in news_list:
                news_list.append(data)

        return news_list

    def write_news(self, data, name):
        with open(name + '.json', 'a', encoding='utf-8') as f:
            content = json.dumps(data, ensure_ascii=False)
            f.write(content)

if __name__ == "__main__":
    url_list = [
        ("通知公告", "http://www.cug.edu.cn/index/tzgg.htm"),
        # ("地大要闻", "http://www.cug.edu.cn/index/ddyw.htm"),
        # ("学术动态", "http://www.cug.edu.cn/index/xsdt.htm"),
    ]
    news_spider = NewsSpider(url_list)
    news_spider.start_work()





