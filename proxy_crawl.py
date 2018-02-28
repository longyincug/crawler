import urllib.request
from lxml import etree
import requests


proxy_list = [

]
for i in range(1,34):
    url = "http://www.66ip.cn/areaindex_" + str(i) + "/1.html"
    headers= {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}
    response = requests.get(url,headers=headers)
    selector = etree.HTML(response.text)
    items = selector.xpath('//table[@bordercolor="#6699ff"]/tr')

    for item in items[1:]:
        word = item.xpath('./td')
        host = word[0].text
        port = word[1].text
        ip = host+':'+port
        proxy_list.append(ip)
print("采集代理完毕")
# print(proxy_list)

count = 0
for each in proxy_list:
    try:
        http_proxy_handler = urllib.request.ProxyHandler({"http" : each})

        opener = urllib.request.build_opener(http_proxy_handler)

        opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]

        response = opener.open("http://www.baidu.com/", timeout=5)

        print(response.read().decode('utf-8'))
        count += 1
        print("已成功 %d 次"%count)
    except Exception as e:
        print(e)
