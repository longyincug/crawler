import urllib.parse
import urllib.request

# 模拟POST请求 百度翻译

# 要通过抓包获取真正的URL请求地址
url = "http://fanyi.baidu.com/sug"

# 模拟完整的请求headers
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
}

# 接收用户输入
key = input("请输入要翻译的内容：")

# 发送到web服务器的表单数据
form_data = {'kw':key}


def spider(url, form_data, headers):
    # 经过转码,注意POST表单数据必须是bytes类型，所以还要经过utf-8编码
    data = urllib.parse.urlencode(form_data).encode('utf-8')

    # Request()方法里的data参数有值，这个请求就是POST请求
    request = urllib.request.Request(url, data=data, headers=headers)

    response = urllib.request.urlopen(request)

    # 返回JSON格式的数据
    return response.read().decode('utf-8')


content = spider(url, form_data, headers)

if len(eval(content)['data']) == 0:

    # 中译英上传的表单数据不同，需要验证， 暂时没法解决sign和token问题
    form_data = {
        "from" : "zh",
        "to" : "en",
        "query" : key,
        "transtype" : "enter",
        "simple_means_flag" : "3",
        # "sign" : ,
        # "token" : ,
    }
    url = "http://fanyi.baidu.com/v2transapi"
    content = spider(url, form_data, headers)
    print(content)
else:
    print(content)
