"""
# https://refactoringguru.cn/design-patterns/factory-method/python/example
工厂只负责贴牌（接口）
实际生成过程还有子厂完成（为每个产品分配一道流水线）

-----------------------
最后产品由工厂配发
-----------------------

产品：每个产品也是独立的，需要子类去实现
"""

from abc import ABC, abstractmethod


class Factory(ABC):

    @abstractmethod
    def factory_method(self):
        """
        must implement
        """
        pass

    def do_operation(self):
        instance_product = self.factory_method()
        return f"execute factory: {instance_product.operation()}"


class ConcreteFactoryA(Factory):
    def factory_method(self):
        """
        concrete factory, it to execute Product
        """
        return ConcreteProductA()


class ConcreteFactoryB(Factory):
    def factory_method(self):
        """
        concrete factory, it to execute Product
        """
        return ConcreteProductB()


class Product(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA(Product):
    def operation(self):
        return "logic operation from productA"


class ConcreteProductB(Product):
    def operation(self):
        return "logic operation from productB"


if __name__ == '__main__':
    """
    client
    客户端只需要调用工厂方法即可 
    由工厂来连接方法
    """
    concreteA = ConcreteFactoryA()
    print(concreteA.do_operation())

    concreteB = ConcreteFactoryB()
    print(concreteB.do_operation())
