# -*- coding: utf-8 -*-
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import MyspiderItem

class Tencent1Spider(CrawlSpider):
    name = 'tencent1'
    allowed_domains = ['hr.tencent.com']
    start_urls = ["http://hr.tencent.com/position.php?&start=0#a"]

    rules = (
        Rule(LinkExtractor(allow='start=\d+'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # i = {}
        # #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # #i['name'] = response.xpath('//div[@id="name"]').extract()
        # #i['description'] = response.xpath('//div[@id="description"]').extract()
        # return i

        for i in response.xpath('//*[@class="even"]'):

            tname = i.xpath('./td[1]/a/text()').extract()[0]
            tlink = i.xpath('./td[1]/a/@href').extract()[0]
            tinfo = i.xpath('./td[2]/text()').extract()[0]
            tlocal = i.xpath('./td[3]/text()').extract()[0]

            # ORM构建
            item = MyspiderItem()
            item['tname'] = tname.encode('utf-8')
            item['tlink'] = tlink.encode('utf-8')
            item['tinfo'] = tinfo.encode('utf-8')
            item['tlocal'] = tlocal.encode('utf-8')

            yield item