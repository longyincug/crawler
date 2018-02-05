import urllib.request
import random

# User-Agent的伪造

# 向指定的url地址发送请求，并返回服务器相应的类文件对象
# response = urllib.request.urlopen("http://www.baidu.com/")

# 但urlopen不支持重构请求报头,需要构造请求对象
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
}
url = "http://www.baidu.com/"

# 可以通过urllib.request.Request()方法构造一个请求对象
# request = urllib.request.Request(url,headers=headers)


# 可以是User-Agent列表，也可以是代理列表
ua_list = [
    "Opera/9.80(WindowsNT6.1;U;en) Presto/2.8.131 Version/11.11",
    "Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;360SE)",
    "Mozilla/5.0(WindowsNT6.1;rv:2.0.1) Gecko/20100101Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Mozilla/5.0(Macintosh;IntelMacOSX10.6;rv:2.0.1) Gecko/20100101Firefox/4.0.1",
]

# 在User-Agent列表里随机选择一个User-Agent
user_agent = random.choice(ua_list)

# 构造一个请求
request = urllib.request.Request(url)

# add_header()方法，添加/修改一个HTTP报头
request.add_header("User-Agent",user_agent)

# get_header() 获取一个已有的HTTP报头的值，注意只能第一个字母大写，其他的必须小写
print(request.get_header("User-agent"))

# response 服务器返回的类文件对象,支持Python文件对象的操作方法
response = urllib.request.urlopen(request)

# read()方法，读取文件里的所有内容，返回bytes类型的数据，需要解码
html = response.read().decode('utf-8')

# print(html)

# 返回HTTP的响应码，成功 返回200
print(response.getcode())

# 返回数据的实际URL，防止重定向问题
print(response.geturl())

# 返回服务器响应的HTTP报头
print(response.info())
