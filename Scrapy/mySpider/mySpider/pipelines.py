# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymongo
import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
# class MyspiderPipeline(object):
#
#     def __init__(self):
#         self.file = open('techer.txt', 'w')
#
#     # 必须实现且必须返回
#     def process_item(self, item, spider):
#         # content = json.dumps(dict(item)) + "\n"
#         content = str(item) + '\n'
#         self.file.write(content)
#         return item
#
#     def close_spider(self, spider):
#         self.file.close()

# class ImagePiple(ImagesPipeline):
#     IMAGES_STORE = get_project_settings().get('IMAGES_STORE')
#
#     def get_media_requests(self, item, info):
#         image_url = item['durl']
#         yield scrapy.Request(image_url)

class MongoPiple():

    def __init__(self):
        client = pymongo.MongoClient(host='localhost', port=27017)
        db = client['douyu']
        self.coll = db['doubanmovie']

    def process_item(self, item, spider):
        data = dict(item)
        self.coll.insert(data)
        return item