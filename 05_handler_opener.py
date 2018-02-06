import urllib.request

# 构建一个HTTPHandler处理器对象，支持处理HTTP的请求
http_handler = urllib.request.HTTPHandler()

# 调用build_opener()方法构建一个自定义的opener对象，可以用来发送请求，参数是构建的处理器对象
opener = urllib.request.build_opener(http_handler)

request = urllib.request.Request("http://www.baidu.com/")

# 和urlopen得到的结果一样
response = opener.open(request)

print(response.read().decode('utf-8'))

