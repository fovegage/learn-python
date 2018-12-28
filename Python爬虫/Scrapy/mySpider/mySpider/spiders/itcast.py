# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#ac']

    # 处理response
    def parse(self, response):
        # 测试
        # filename = 'tech.html'
        # open(filename, 'wb').write(response.body)
        # items = []
        for each in response.xpath('//div[@class="li_txt"]'):
            item = MyspiderItem()

            name = each.xpath('h3/text()').extract()
            level = each.xpath('h4/text()').extract()
            info = each.xpath('p/text()').extract()

            item['name'] = name[0]
            item['level'] = level[0]
            item['info'] = info[0]

            # items.append(item)

            yield item

        # return items
