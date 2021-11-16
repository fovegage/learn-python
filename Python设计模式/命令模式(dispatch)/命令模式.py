# https://www.starky.ltd/2020/12/26/python-design-patterns-command-pattern/

"""

股票交易中
用户 代理（券商）   操作购买  操作售出 （交易所接口）
"""

from abc import abstractmethod


class Exchange:
    @abstractmethod
    def execute(self):
        """
        交易所接口 必须实现
        """


# 分别实现 购买 售出操作
class BuyOperate(Exchange):
    def __init__(self, trade):
        self.trade = trade

    def execute(self):
        self.trade.buy()


class SellOperate(Exchange):
    def __init__(self, trade):
        self.trade = trade

    def execute(self):
        self.trade.sell()


class Broker:
    @staticmethod
    def place_order(order):
        """
        券商执行 具体操作
        """
        order.execute()


# 可以进一步抽象 必须要实现的业务
class StockTrade:
    """
    具体策略用户实现  比如购买多少 买那个股票
    """
    def buy(self):
        print('buy')

    def sell(self):
        print('sell')


if __name__ == '__main__':
    """
    代码思想  
    需要维护 多个类   每个类实现规定的接口
    一个类一个任务   代码解耦    一个实现类 实现所有的业务
    然后让 中间人 去顺序执行
    可以使用 队列
    """
    trade = StockTrade()  # 具体业务类
    buy = BuyOperate(trade)  # 只实例化  trade.buy
    sell = SellOperate(trade)

    broker = Broker()
    broker.place_order(buy)  # 触发 trade.buy
    broker.place_order(sell)
