# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']

    def start_requests(self):
        url = 'http://www.renren.com/SysHome.do'

        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url=url,
            formdata={"email": "18553713028", "password": "416798gao"},
            callback=self.parse_page
        )

    def parse_page(self, response):
        print(response.body)

