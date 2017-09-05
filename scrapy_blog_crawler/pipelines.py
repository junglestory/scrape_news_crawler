# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from __future__ import unicode_literals
import json
import codecs

class ScrapyBlogCrawlerPipeline(object):
    def __init__(self):
        self.file = codecs.open('blog.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.file.write(line)  # 파일에 기록
        return item

    def spider_closed(self, spider):
        self.file.close()  # 파일 CLOSE