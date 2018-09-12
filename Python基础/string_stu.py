# -*- coding:utf-8 -*-
# https://movie.douban.com/j/chart/top_list?type=24&interval_id=50%3A40&action=&start=40&limit=20
import urllib2
import urllib

url='https://movie.douban.com/j/chart/top_list?type=24&interval_id=50%3A40&action'

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS... "}

fromdata={
    'start':'40',
    'limit':'20'
}

data=urllib.urlencode(fromdata)

request=urllib2.Request(url,data=data,headers=header)

print(urllib2.urlopen(request).read())