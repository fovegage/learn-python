# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyspiderItem(scrapy.Item):
    # itcast define
    name = scrapy.Field()
    level = scrapy.Field()
    info = scrapy.Field()

    # tencent define
    tname= scrapy.Field()
    tlink = scrapy.Field()
    tinfo = scrapy.Field()
    tlocal = scrapy.Field()




