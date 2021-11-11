from abc import ABC, abstractmethod

"""
参考文档
https://www.starky.ltd/2020/12/25/python-design-patterns-proxy-pattern/
"""


class Payment(ABC):

    @abstractmethod
    def do_buy(self, ticket):
        """
        must implement
        """


class ScenicArea(Payment):
    """
    真正的出票处
    """

    def __init__(self):
        self.tickets = 100

    def check(self):
        if self.tickets < 0:
            return False
        return True

    @property
    def modify_tickets(self):
        return self.tickets

    @modify_tickets.setter
    def modify_tickets(self, ticket):
        self.tickets -= ticket

    def do_buy(self, ticket):
        status = self.check()
        if status:
            print('buy success')
            self.modify_tickets = ticket
        else:
            print('buy fail')


class TravelAgency(Payment):
    """
    代理出票处
    """

    def __init__(self):
        # 构造方法 实例化真正操作的对象
        self.scenic = ScenicArea()

    def do_buy(self, ticket):
        self.scenic.do_buy(ticket)


class Tourist:
    def __init__(self):
        self.travel = TravelAgency()

    def make_pay(self):
        self.travel.do_buy(9)


if __name__ == '__main__':
    """
    加入 我去买景点门票  我需要一个代理商去购买 
    
    在 价格一样的情况下消费者看来  代理商出票和  景区出票 是一回事   程序中就是继承于同一个基类
    
    寻找方是发出请求的一方   提供方是根据请求提供资源的一方
    """
    tourist = Tourist()
    tourist.make_pay()
