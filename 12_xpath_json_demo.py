# 用xpath爬取糗事百科里面段子的详情，存储为json格式
# https://www.qiushibaike.com/8hr/page/1/
# 每个段子 //div[contains(@id,"qiushi_tag_")]
# 用户名   ./div/a/h2
# 图片链接 ./div/a/img[@class="illustration"]/@src
# 段子内容 ./a/div[@class="content"]/span
# 点赞数 ./div/span/i[@class="number"]
# 评论数 ./div/span/a/i[@class="number"]

import requests
from lxml import etree
import json

def write_item(data):
    content = json.dumps(data, ensure_ascii=False)
    with open('stories.json','a', encoding='utf-8') as f:
        f.write(content + '\n')

def deal_item(selector):
    items = selector.xpath('//div[contains(@id,"qiushi_tag_")]')

    for item in items:
        # 可能有匿名用户
        username = item.xpath('./div[@class="author clearfix"]//h2')[0].text
        img = item.xpath('./div/a/img[@class="illustration"]/@src')
        # 忽略内容中的br，获取标签下的所有内容，用'string(.)'
        content = item.xpath('./a/div[@class="content"]/span')[0].xpath('string(.)')
        # content = item.xpath('./a/div[@class="content"]/span//text()')
        good = item.xpath('./div/span/i[@class="number"]')[0].text
        comment = item.xpath('./div/span/a/i[@class="number"]')[0].text

        data = {
            'user':username,
            'img':img,
            'content':content,
            'good':good,
            'comment':comment,
        }
        write_item(data)

def main():
    # 爬取糗事百科前10页的内容
    for page in range(1, 11):

        url = "https://www.qiushibaike.com/8hr/page/"+ str(page) +"/"

        headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"}

        response = requests.get(url, headers=headers)

        selector = etree.HTML(response.content)

        deal_item(selector)

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    end_time = time.time()
    print("爬取解析工作共耗时%s秒" % str(end_time - start_time))
