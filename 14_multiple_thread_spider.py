import requests
import threading
from queue import Queue
from lxml import etree
import json


class CrawlThread(threading.Thread):
    def __init__(self, threadName, data_queue, pageQueue):
        super(CrawlThread, self).__init__()
        self.threadName = threadName
        self.data_queue = data_queue
        self.pageQueue = pageQueue
        self.headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"}

    def run(self):
        # print("%s启动"%self.threadName)
        while not CRAWL_EXIT:
            try:
                # block设置为False，当队列中为空，会抛出异常
                page = self.pageQueue.get(False)
                url = "https://www.qiushibaike.com/8hr/page/" + str(page) + "/"
                response = requests.get(url, headers=self.headers)
                # 将爬取下来的网页内容存入待解析数据队列
                self.data_queue.put(response.content)
            except Exception as e:
                # print(e)
                pass
        # print("%s结束"%self.threadName)


class ParseThread(threading.Thread):
    def __init__(self, threadName, data_queue, file, lock):
        super(ParseThread, self).__init__()
        self.threadName = threadName
        self.data_queue = data_queue
        self.file = file
        self.lock = lock

    def run(self):
        # print("%s启动"%self.threadName)
        while not PARSE_EXIT:
            try:
                content = self.data_queue.get(False)
                self.parse(content)
            except Exception as e:
                # print(e)
                pass
        # print("%s结束"%self.threadName)

    def parse(self, content):
        try:
            selector = etree.HTML(content)
            items = selector.xpath('//div[contains(@id,"qiushi_tag_")]')

            for item in items:
                # 可能有匿名用户
                username = item.xpath('./div[@class="author clearfix"]//h2')[0].text
                img = item.xpath('./div/a/img[@class="illustration"]/@src')
                # 忽略内容中的br，获取标签下的所有内容，用'string(.)'
                content = item.xpath('./a/div[@class="content"]/span')[0].xpath('string(.)')
                good = item.xpath('./div/span/i[@class="number"]')[0].text
                comment = item.xpath('./div/span/a/i[@class="number"]')[0].text

                data = {
                    'user': username,
                    'img': img,
                    'content': content,
                    'good': good,
                    'comment': comment,
                }

                with self.lock:
                    self.file.write(json.dumps(data, ensure_ascii=False) + '\n')

        except Exception as e:
            # print(e)
            pass

CRAWL_EXIT = False
PARSE_EXIT = False


def main():
    # 将需要爬取的网页页码存入待爬取队列（10页）
    pageQueue = Queue(10)
    for i in range(1, 11):
        pageQueue.put(i)

    # 待解析队列
    data_queue = Queue()

    # 存储3个爬取线程的名字
    thread_name_list = ['爬取线程1', '爬取线程2', '爬取线程3']

    # 用来存储3个正在爬取的线程
    crawl_thread_list = []

    for threadName in thread_name_list:
        thread = CrawlThread(threadName, data_queue, pageQueue)
        thread.start()
        crawl_thread_list.append(thread)


    # 三个解析线程
    parse_thread_name = ['解析线程1', '解析线程2', '解析线程3']

    parse_thread_list = []

    # 创建文件对象，用来写入解析内容
    file = open('content.json', 'a', encoding='utf-8')

    # 创建一个互斥锁，防止线程之间操作文件发生错乱
    lock = threading.Lock()

    for threadName in parse_thread_name:
        thread = ParseThread(threadName, data_queue, file, lock)
        thread.start()
        parse_thread_list.append(thread)

    # 等待, 如果页码队列为空，停止爬取
    while True:
        if pageQueue.empty():
            global CRAWL_EXIT
            CRAWL_EXIT = True
            break

    # 堵塞，等待所有的爬取线程完成任务
    for each_thread in crawl_thread_list:
        each_thread.join()

    while True:
        if data_queue.empty():
            global PARSE_EXIT
            PARSE_EXIT = True
            break

    for each_thread in parse_thread_list:
        each_thread.join()

    with lock:
        file.close()


if __name__ == "__main__":
    import time
    start_time = time.time()
    main()
    end_time = time.time()
    print("爬取解析工作共耗时%s秒"%str(end_time - start_time))
