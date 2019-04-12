# -*- coding: utf-8 -*-
# @Time    : 2019/4/11 17:02
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : etree_stu.py
# @Software: PyCharm


from xml.etree.ElementTree import parse
from urllib.request import urlopen


xml_con = urlopen('http://planet.python.org/rss20.xml')
parse_xml = parse(xml_con)

for item in parse_xml.iterfind('channel/item'):
    print(item.findtext('title'))