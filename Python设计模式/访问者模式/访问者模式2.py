"""

使用访问者模式 实现 http

用 http
"""
from abc import ABC, abstractmethod


class HTTP(ABC):
    @abstractmethod
    def accept(self, visitor, method):
        pass


class DoBaidu(HTTP):
    @classmethod
    def accept(cls, visitor, method):
        getattr(visitor, method)()


class DoTencent(HTTP):
    def accept(self, visitor, method):
        visitor.post()


class Visitor(ABC):
    @abstractmethod
    def get(self):
        pass

    @abstractmethod
    def post(self):
        pass

    @abstractmethod
    def put(self):
        pass

    @abstractmethod
    def delete(self):
        pass


class BaiduVisitor(Visitor):
    def get(self):
        print('baidu get')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


class TencentVisitor(Visitor):
    def get(self):
        print('tencent get')

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass


def client(services, visitor):
    for service in services:
        service.accept(visitor)


if __name__ == '__main__':
    # https://juejin.cn/post/6844903670220324878
    # https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p21_implementing_visitor_pattern.html
    # services = [GET(), POST()]
    # visitor_baidu = BaiduVisitor()
    # client(services, visitor_baidu)

    visitor_baidu = BaiduVisitor()  # 实现具体的业务
    DoBaidu.accept(visitor_baidu, 'get')  # 访问具体的业务
