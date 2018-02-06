import urllib.request

# 代理开关，表示是否启用代理
proxy_switch = True

# 构建一个Handler处理器对象，参数是字典类型，包括代理类型和代理服务器的IP+PORT
http_proxy_handler = urllib.request.ProxyHandler({"http" : "47.52.222.165:80"})

# 如果是私密代理
# http_proxy_handler = urllib.request.ProxyHandler({"http" : "username:password@IP:Port"})
# 一般可以把账号密码存入~.bash_profile,系统环境变量中，需要用时，os.environ.get("proxy_user")即可


# 一个没有代理的处理器对象
null_proxy_handler = urllib.request.ProxyHandler({})

if proxy_switch:
    opener = urllib.request.build_opener(http_proxy_handler)
else:
    opener = urllib.request.build_opener(null_proxy_handler)

# 构建一个全局的opener，之后的所有请求都可以用urlopen()去发送，同时附带Handler的功能
urllib.request.install_opener(opener)

response = urllib.request.urlopen("http://www.baidu.com/")

print(response.read().decode('utf-8'))
