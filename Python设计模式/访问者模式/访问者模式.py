"""
访问者模式实现
https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p21_implementing_visitor_pattern.html


使用 加减乘除 来模拟
"""


class Session:
    """
    基类  最终要访问的对象
    """

    def request(self, url, method):
        print(url, method)

    def post(self, url, method):
        self.request(url, method)

    def get(self, url, method):
        self.request(url, method)


class RequestVisitor:
    def __init__(self):
        self.session = Session()

    def visit(self, url, method):
        # method = getattr(self, method)
        return self.session.get(url, method)


# 装饰器 回参
class Visitor(RequestVisitor):
    def get(self, url, method):
        return self.visit(url, method)


if __name__ == '__main__':
    """
    可以通过 反射的方式对  类对象进行管理  而不是  if else  这便是 访问者模式
    
    将由一个访问者类 进行统一管理  访问者类并不和基类方法交互
    而是让 实现类与其交互    实现类调用访问类   
    
    requests 库 便使用 访问者模式进行代码组织 requests.get()
    
    
    访问者模式演进
    
    
    """
    visitor = Visitor()
    visitor.get('https://www.baidu.com', 'GET')
