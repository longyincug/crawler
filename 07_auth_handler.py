# HTTPPasswordMgrWithDefaultRealm()类将创建一个密码管理对象，用来保存 HTTP 请求相关的用户名和密码，主要应用两个场景：
    # 验证代理授权的用户名和密码 处理器 (ProxyBasicAuthHandler())
    # 验证Web客户端的的用户名和密码 处理器 (HTTPBasicAuthHandler())

import urllib.request

username = 'test'
password = '123456'
webserver = "192.168.0.113"

# 构建一个密码管理对象，可以用来保存和HTTP请求相关的授权账户信息
passwordMgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# 添加授权账户信息,第一个参数realm如果没有指定就写None，后三个分别是站点IP，账户名和密码
passwordMgr.add_password(None, webserver, username, password)

# HttpBasicAuthHandler() HTTP基础验证处理器类
http_auth_handler = urllib.request.HTTPBasicAuthHandler(passwordMgr)

# 当然也可以创建代理授权验证的处理器
# proxy_auth_handler = urllib.request.ProxyBasicAuthHandler(passwordMgr)

# 构建自定义opener（可以同时加入代理基础验证和HTTP基础验证等多个处理器）
opener = urllib.request.build_opener(http_auth_handler)

request = urllib.request.Request("http://" + webserver + "/")

# 用授权验证信息
response = opener.open(request)

