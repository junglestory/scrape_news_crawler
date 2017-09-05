# -*- coding: utf-8 -*-
import scrapy
import time
import re
from scrapy_blog_crawler.items import BlogItem

MAX_LOOP = 10
pageNo = 1

class NewsSpider(scrapy.Spider):
    name = "blog"
    start_urls = [
        'https://section.blog.naver.com/main/DirectoryPostList.nhn?option.directorySeq=28'
    ]

    def parse(self, response):
        global pageNo

        for blog in response.xpath('//*[@id="content"]/form/div/div[@class="attention_post"]/ul/li'):
            item = BlogItem()

            item['title'] = blog.xpath('h5/a/text()').extract()[0]
            item['url'] = blog.xpath('h5/a/@href').extract()[0]
            item['author'] = blog.xpath('div/a/text()').extract()[0]
            item['date'] = blog.xpath('div[@class="list_data _eachPost"]/span/text()').extract()[0]
            item['desc'] = blog.xpath('div[@class="list_content"]/div/a[@class="template_briefContents"]/text()').extract()[0]

            item['title'] = re.sub('\t', '', item['title']).strip()
            item['desc'] = re.sub('\n', '', item['desc']).strip()
            item['date'] = re.sub('. ', '', item['date']).strip()

            time.sleep(1)
            yield item

        # next_page_no = response.xpath('//*[@id="mArticle"]/div[@class="box_etc"]/div/span/em/text()')
        # print(next_page_no)
        pageNo += 1

        if pageNo <= MAX_LOOP:
            next_page_url = "https://section.blog.naver.com/main/DirectoryPostList.nhn?option.page.currentPage=" + str(pageNo) + "&option.directorySeq=28"
            yield scrapy.Request(response.urljoin(next_page_url))

