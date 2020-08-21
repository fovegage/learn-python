"""
getattr
https://www.jb51.net/article/87073.htm
https://www.jianshu.com/p/dec562715df6
"""


class Link:
    def __init__(self, url):
        self.url = url

    def __getattr__(self, item):
        if item == 'get' or item == 'post':
            pass
            # print(self.url)
        return Link('{}.{}'.format(self.url, item))


link = Link('admin')
print(link.get.post)