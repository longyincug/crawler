# http://www.lagou.com/lbs/getAllCitySearchLabels.json
# 利用JSONPATH获取一个JSON文件中指定属性的所有值,(先要loads将json转化为python对象)

import requests
import json
import jsonpath
import chardet

# url = "http://www.lagou.com/lbs/getAllCitySearchLabels.json"
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"}
response = requests.get(url, headers=headers)

# 产生的是字节码数据，编码为utf-8
html = response.content
# print(chardet.detect(html))

# 产生的是字符串数据，为Unicode字符串
text = response.text
# print(html.decode('utf-8') == text)

# 将JSON数据转换为python对象
content = json.loads(text)

# 进行jsonpath匹配
movies = jsonpath.jsonpath(content, '$..title')
print(movies)

# 以json文件形式写入本地（数组）
# with open('name.json', 'w') as f:
    # f.write(json.dumps(movies, ensure_ascii=False))

