"""
暴露一个方法  接入不同的能力
# https://refactoringguru.cn/design-patterns/strategy/python/example
"""
from abc import ABC


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy):
        self._strategy = strategy

    def operation(self):
        """
        执行具体的算法
        """
        data = [3, 1, 2]
        return self._strategy.do_algorithm(data)


class Strategy(ABC):
    def do_algorithm(self, data: list):
        pass


class SortStrategy(Strategy):
    def do_algorithm(self, data: list):
        return sorted(data)


class ReverseStrategy(Strategy):
    def do_algorithm(self, data: list):
        return list(reversed(sorted(data)))


if __name__ == '__main__':
    context = Context(SortStrategy())
    print(context.operation())

    context.strategy = ReverseStrategy()
    print(context.operation())
