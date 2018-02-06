import urllib.request

# ajax方式加载的页面，数据来源一定是JSON

# 豆瓣电影排行榜，剧情类,通过抓包获取JSON数据来源的URL：
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}

request = urllib.request.Request(url, headers=headers)

response = urllib.request.urlopen(request)

print(response.read().decode('utf-8'))
