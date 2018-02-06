# urllib的urlencode()接收字典作为一个参数
# {}
# URL的编码工作使用urllib.parse的urlencode()函数，帮我们将key:value这样的键值对转换成"key=value"这样的字符串，
# 解码工作可以使用urllib.parse的unquote()函数

import urllib.parse
import urllib.request

def load_pages(url,filename):
    """
        根据url来爬取指定页面的内容
    """
    print("正在下载%s"%filename)
    headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.urlopen(request).read().decode('utf-8')

def write_pages(html,filename):
    """
        将爬取下来的内容保存至本地
    """
    print("正在保存%s"%filename)
    with open(filename+'.html','w',encoding='utf-8') as f:
        f.write(html)
    print('-'*20)

def tieba_spider(url,beginPage,endPage):
    """
        爬虫调度器，负责接收需求，控制爬取。
        url: 要爬取的贴吧的前半部分url
        beginPage: 要爬取的起始页
        endPage: 要爬取的结束页
    """
    for page in range(beginPage, endPage + 1):
        last_url = '&pn='+ str((page-1)*50)
        full_url = url + last_url
        html = load_pages(full_url,"第%d页"%page)
        write_pages(html, "第%d页"%page)
    print("爬取完毕")

if __name__ == '__main__':
    key = input("请输入需要爬取的贴吧名：")
    beginPage = int(input("请输入需要爬取的起始页："))
    endPage = int(input("请输入需要爬取的终止页："))
    url = "http://tieba.baidu.com/f?"
    key = urllib.parse.urlencode({'kw':key})
    full_url = url + key
    tieba_spider(full_url, beginPage, endPage)
