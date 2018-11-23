# -*- coding: utf-8 -*-
import scrapy
from ..items import MyspiderItem
import re

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencnet.com']
    start_urls = ['http://hr.tencent.com/position.php?&start=0#a']

    def parse(self, response):

        #遍历网页
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

            # 将链接不断加入待爬队列
            # curpage = re.search('(\d+)', response.url).group(1)
            # page = int(curpage) + 10
            # url = re.sub('\d+', str(page), response.url)

            # 将链接不断加入待爬队列,直到4XX/5XX
            url = 'http://hr.tencent.com/position.php?&start=40#a'
            yield scrapy.Request(url, callback=self.parse)

            # 生成迭代器  不用return
            yield item

