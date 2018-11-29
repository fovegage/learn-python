# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://stackoverflow.com/questions?sort=votes']

    def parse(self, response):
        for href in response.css('.question-summary h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_question)

    def parse_question(self, response):

        tname = response.css('h1 a::text').extract()[0],
        tinfo = response.css('.question .vote-count-post::text').extract()[0]
        tlocal = response.css('.question .post-tag::text').extract()
        tlink = response.url

        # ORM构建
        item = MyspiderItem()
        item['tname'] = tname.encode('utf-8')
        item['tlink'] = tlink.encode('utf-8')
        item['tinfo'] = tinfo.encode('utf-8')
        item['tlocal'] = tlocal.encode('utf-8')
        print(tname)
        yield item
