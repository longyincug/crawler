# crawler
learn how to write the python crawler


**网络爬虫根据使用场景分为通用爬虫和聚焦爬虫：**

1. 通用爬虫：搜索引擎用的爬虫系统

    - 目标：尽可能的把互联网上的所有网页下载下来，放到本地服务器里形成备份（百度快照），
        再对这些网页做相关处理（提取关键字、去掉广告），最后提供一个用户检索接口。
        
    - 抓取流程：
        1. 选取一部分已有的URL，把这些URL放入待爬取队列
        2. 从队列里取出这些URL，然后解析DNS得到主机IP，然后去这个IP对应的服务器里下载HTML页面，
            保存到搜索引擎的本地服务器
        3. 分析这些网页内容，找出网页里其他的URL链接，继续执行第二步，直到爬取条件结束
    
    - 搜索引擎如何获取一个新网站的URL：
        1. 主动向搜索引擎提交网址：http://zhanzhang.baidu.com/linksubmit/url
        2. 在其他网站设置网站的外链
        3. 搜索引擎会和DNS服务商进行合作，可以快速收录新的网站
        
    - 通用爬虫要遵守规则：Robots协议
    
    - 工作流程：爬取网页--存储数据--内容处理--提供检索/排名服务
    
    - 搜索引擎排名：
        1. PageRank值：根据网站的流量（点击量、浏览量、人气）统计，流量越高，排名越靠前
        2. 竞价排名：用钱来提高排名
        
    - 通用爬虫缺点：
        1. 只能提供和文本相关的内容，不能提供多媒体和二进制（程序、脚本）文件
        2. 提供结果千篇一律，不能针对不同背景领域的人提供不同的搜索结果
        3. 不能理解人类语义上的检索
        
2. 聚焦爬虫：
    - 爬虫程序员写的针对某种内容的爬虫
    - 面向主题、面向需求

***

**Handler处理器 和 自定义Opener**

- opener是 urllib.request.OpenerDirector 的实例，我们之前一直都在使用的urlopen，它是一个特殊的opener（也就是模块帮我们构建好的）。

- 但是基本的urlopen()方法不支持代理、cookie等其他的HTTP/HTTPS高级功能。
所以要支持这些功能：

1. 使用相关的 **Handler处理器** 来创建特定功能的处理器对象；
2. 然后通过 **urllib2.build_opener()** 方法使用这些处理器对象，创建自定义opener对象（可以接受多个处理器）；
3. 使用自定义的opener对象，调用 **open()** 方法发送请求。

- 如果程序里所有的请求都使用自定义的opener，可以使用urllib.request.install_opener() 将自定义的opener对象定义为全局opener，表示如果之后凡是调用urlopen，都将使用这个opener（根据自己的需求来选择）

***

**HTTPPasswordMgrWithDefaultRealm()**

这个类将创建一个密码管理对象，用来保存和HTTP请求相关的用户名和密码，主要应用两个场景：

- 验证代理授权的用户名和密码 (ProxyBasicAuthHandler())
- 验证Web客户端的的用户名和密码 (HTTPBasicAuthHandler())

***

**cookielib库 和 HTTPCookieProcessor处理器**

在Python处理Cookie，一般是通过cookielib模块(python3中为http.cookiejar)和 urllib.request模块的HTTPCookieProcessor处理器类一起使用。

- cookielib模块：主要作用是提供用于存储cookie的对象

- HTTPCookieProcessor处理器：主要作用是处理这些cookie对象，并构建handler对象。

***

**非结构化的数据处理**

先有数据，再有结构

- 文本、电话号码、邮箱地址
    - 正则表达式
    
- HTML 文件
    - 正则表达式
    - XPath
    - CSS选择器

**结构化的数据处理**

先有结构、再有数据

- JSON 文件
    - JSON Path
    - 转化成Python类型进行操作（json类）

- XML 文件
    - 转化成Python类型（xmltodict）
    - XPath
    - CSS选择器
    - 正则表达式
    
***

**数据提取之JSON与JsonPATH**

JSON(JavaScript Object Notation) 是一种轻量级的数据交换格式，它使得人们很容易的进行阅读和编写。同时也方便了机器进行解析和生成。适用于进行数据交互的场景，比如网站前台与后台之间的数据交互。

json简单说就是javascript中的对象和数组，所以这两种结构就是对象和数组两种结构，通过这两种结构可以表示各种复杂的结构

- 对象：

    对象在js中表示为{ }括起来的内容，数据结构为 { key：value, key：value, ... }的键值对的结构，在面向对象的语言中，key为对象的属性，value为对应的属性值，所以很容易理解，取值方法为 对象.key 获取属性值，这个属性值的类型可以是数字、字符串、数组、对象这几种。

- 数组：
    
    数组在js中是中括号[ ]括起来的内容，数据结构为 ["Python", "javascript", "C++", ...]，取值方式和所有语言中一样，使用索引获取，字段值的类型可以是 数字、字符串、数组、对象几种。


**import JSON**

- json.dumps()
    
    实现python类型转化为json字符串

- json.loads()
    
    把Json格式字符串解码转换成Python对象 
    
**JsonPath**

- JsonPath 是一种信息抽取类库，是从JSON文档中抽取指定信息的工具，提供多种语言实现版本，包括：Javascript, Python， PHP 和 Java。

- JsonPath 对于 JSON 来说，相当于 XPATH 对于 XML。