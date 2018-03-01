# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class QiushiPipeline(object):
    # 可选，作为类的初始化方法
    def __init__(self):
        self.file = open('qiushi.json', 'w', encoding='utf-8')
    
    # 处理item数据，process_item 必须要写
    def process_item(self, item, spider):
        jsontext = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(jsontext + '\n')
    
    # 可选，处理结束时调用该方法，注意参数
    def close_spider(self, spider):
        self.file.close()

