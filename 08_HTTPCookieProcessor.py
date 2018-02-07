import http.cookiejar
import urllib.request
import urllib.parse

# 通过CookieJar()类构建一个对象，用来保存cookie的值
cookie = http.cookiejar.CookieJar()

# 通过HTTPCookieProcessor()处理器构建一个处理器对象，用来处理cookie
# 参数就是构建的CookieJar()对象
cookie_handler = urllib.request.HTTPCookieProcessor(cookie)

opener = urllib.request.build_opener(cookie_handler)

# 对于opener对象，也可以直接通过给属性赋值（列表），来添加headers参数(元组的形式)
opener.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")]

# renren网的登录接口 (现在大多数网站已采用sign+token验证方式，这种获取cookie直接登录的方式行不通)
url = "http://www.renren.com/PLogin.do"

# 需要登录的账号密码
data = {'email':'123@163.com', 'password':'123'}

# 通过urlencode()编码转换
data = urllib.parse.urlencode(data).encode('utf-8')

# 构造post请求，发送需要登录的参数，获取cookie
request = urllib.request.Request(url, data=data)

# 发送post请求，如果登录成功，生成登录后的cookie
response = opener.open(request)

# 第二次请求可以是get请求，这个请求将之前生成的cookie一并发给web服务器，服务器会验证cookie通过
response_2 = opener.open("http://www.renren.com/123456/profile")
