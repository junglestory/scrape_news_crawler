# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyBlogCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()      # 제목
    category = scrapy.Field()   # 주제
    url = scrapy.Field()        # 블로그 주소
    author = scrapy.Field()     # 저자
    desc = scrapy.Field()       # 내용
    date = scrapy.Field()       # 작성일
    pass
