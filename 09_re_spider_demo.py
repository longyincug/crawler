import urllib.request
import re

# 用正则爬取内涵段子的小demo

class Spider():
    def __init__(self):
        self.page = 1
        self.switch = True

    def load_page(self):
        """
            根据url下载指定网页的html内容
        """
        url = "http://www.neihanpa.com/article/list_5_" + str(self.page) + ".html"
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
        request = urllib.request.Request(url, headers=headers)
        response = urllib.request.urlopen(request)
        html = response.read().decode('gb2312')
        self.deal_page(html)

    def deal_page(self, html):
        """
            将爬取下来的内容进行处理
        """
        # 建立正则匹配规则, re.S表示全文匹配
        pattern = re.compile('<div\sclass="f18 mb20">(.*?)</div>', re.S)

        # 用规则去html源码中匹配出有效内容
        content_list = pattern.findall(html)
        # print(content_list)

        # 对每个匹配项进行简单的处理，替换掉非法字符
        for item in content_list:
            content = item.replace('<p>', '').replace('</p>', '').replace('<br>','').replace('<br />','')
            # print(content)
            self.write_page(content)

    def write_page(self, content):
        """
            将处理后的内容保存到本地
        """
        with open('stories.txt', 'a', encoding='utf-8') as f:
            f.write(content)

    def start_work(self):
        """
            爬取工作的控制器
        """
        while self.switch:
            self.load_page()
            self.page += 1
            command = input("需要继续爬取请按回车(退出输入quit): ")
            if command == "quit":
                self.switch = False


if __name__ == "__main__":
    duanziSpider = Spider()
    duanziSpider.start_work()
