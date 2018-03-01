import scrapy
from mySpider.items import MyspiderItem

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        #content_list = [] 
        # 不加extract()结果为xpath匹配对象
        for each in response.xpath('//div[contains(@class,"article block untagged mb15")]'):
            item = MyspiderItem() 
            name = each.xpath('.//h2/text()')[0].extract()
            img = each.xpath('./div[@class="author clearfix"]//img/@src')[0].extract()
            content = each.xpath('.//div[@class="content"]/span/text()')[0].extract()
            #print(name, img, content)
            
            item['name'] = name
            item['img'] = img
            item['content'] = content
            #content_list.append(item)
            # 把数据转到pipeline进行处理
            yield item

        #return content_list
            


