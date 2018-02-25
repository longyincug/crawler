import scrapy

class QiushiSpider(scrapy.Spider):
    name = 'qiushi'
    allowed_domains = ['https://www.qiushibaike.com/']
    start_urls = ['https://www.qiushibaike.com/']

    def parse(self, response):
        # 不加extract()结果为xpath匹配对象
        for each in response.xpath('//div[contains(@class,"article block untagged mb15")]'):
            name = each.xpath('.//h2/text()')[0].extract()
            img = each.xpath('./div[@class="author clearfix"]//img/@src')[0].extract()
            content = each.xpath('.//div[@class="content"]/span/text()')[0].extract()
            print(name, img, content)
