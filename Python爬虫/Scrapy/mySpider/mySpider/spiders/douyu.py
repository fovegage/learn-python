# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import MyspiderItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']

    offset = 0
    url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    start_urls = [url + str(offset)]

    def parse(self, response):
        data = json.loads(response.text)['data']

        item = MyspiderItem()
        for each in data:
            item['dname'] = each['nickname']
            item['durl'] = each['vertical_src']

            yield item

        self.offset += 20
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


