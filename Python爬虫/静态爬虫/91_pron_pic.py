# -*- coding: utf-8 -*-
# @Time    : 2018/9/16 17:24
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : 91_pron_pic.py
# @Software: PyCharm

import urllib.request
from lxml import etree
import os
import requests
import random
import string


"""
91pron图片站爬虫
"""


class Pron_91():
    def __init__(self, url):
        self.url = url
        self.domain = "http://" + str(self.url).split('/')[2] + "/"
        self.ua_header = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1 Trident/5.0;"}

    def craw_urls(self):
        request = urllib.request.Request(self.url, headers=self.ua_header)
        response = urllib.request.urlopen(request)
        xmlselector = etree.HTML(response.read().decode('utf-8'))
        urls = set(xmlselector.xpath('//div/a[@style="font-weight: bold;color: purple"]/@href'))
        urls_list = []
        for url in urls:
            urls_list.append(self.domain + url)
        return urls_list

    def random_file_name(self):
        return ''.join(random.sample(string.ascii_letters + string.digits, 12))

    def craw_pic(self):

        for link in self.craw_urls():
            request = urllib.request.Request(link, headers=self.ua_header)
            response = urllib.request.urlopen(request)
            xmlselector = etree.HTML(response.read().decode('utf-8'))
            title = xmlselector.xpath('//h1')
            if str(title[0].text) in os.listdir('G:\\91\\'):
                print('{} --- 资源在文件夹中,将解析下一个'.format(str(title[0].text)))
                continue
            elif str(title[0].text).find("/") > 0:
                tihuan = str(title[0].text).replace('/', '_')
                if tihuan in os.listdir('G:\\91\\'):
                    continue
                os.mkdir('G:\\91\\' + tihuan)
                print(tihuan + "   --->   文件夹创建完成")
                pic = xmlselector.xpath('//div[@class="t_attach"]/a/@href')
                print("共{}张图片,请等待......".format(pic))
                x = 1
                for i in pic:
                    print("正在下载第{}图片".format(x))
                    r = requests.get(self.domain + str(i))
                    with open("G:\\91\\" + tihuan + "\\{}.jpg".format(self.random_file_name()), 'wb') as f:
                        f.write(r.content)
                    x += 1
                print(tihuan + "   --->   已经下载完毕")
                print("-" * 30)

            else:
                if str(title[0].text) in os.listdir('G:\\91\\'):
                    print('{} --- 资源在文件夹中,将解析下一个'.format(str(title[0].text)))
                    continue
                elif str(title[0].text).endswith(".") == True:
                    print('{} --- 资源在文件夹中,将解析下一个'.format(str(title[0].text)))
                    continue
                os.mkdir('G:\\91\\' + title[0].text)
                print(title[0].text + "   --->   文件夹创建完成")
                pic = xmlselector.xpath('//div[@class="t_attach"]/a/@href')
                if len(pic) == 0:
                    continue
                print("共{}张图片,请等待......".format(len(pic)))
                x = 1
                for i in pic:
                    print("正在下载第{}图片".format(x))
                    r = requests.get(self.domain + str(i))
                    with open("G:\\91\\" + title[0].text + "\\{}.jpg".format(self.random_file_name()), 'wb') as f:
                        f.write(r.content)
                    x += 1
                print(title[0].text + "   --->   已经下载完毕")
                print("-" * 30)


if __name__ == '__main__':
    pron = Pron_91("http://f.p03.space/index.php")
    pron.craw_pic()
