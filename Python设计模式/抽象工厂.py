"""
# https://refactoringguru.cn/design-patterns/abstract-factory/python/example
由顶层的抽象工厂先预定义好各个产品

----------------------------
任然由工厂继承类分发
----------------------------

此时的产品类可以取调用其他产品类的方法
"""
from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def do_product_a(self):
        pass

    @abstractmethod
    def do_product_b(self):
        pass


class ConcreteAbstractFactoryA(AbstractFactory):
    def do_product_a(self):
        return ConcreteProductA1()

    def do_product_b(self):
        return ConcreteProductA2()


class ConcreteAbstractFactoryB(AbstractFactory):
    def do_product_a(self):
        return ConcreteProductB1()

    def do_product_b(self):
        return ConcreteProductB2()


class ProductA(ABC):
    @abstractmethod
    def operation(self):
        pass


class ConcreteProductA1(ProductA):
    def operation(self):
        return "logic operation from productA1"


class ConcreteProductA2(ProductA):
    def operation(self):
        return "logic operation from productA2"


class ProductB(ABC):
    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def another_operation(self, concrete: ProductA):
        pass


class ConcreteProductB1(ProductB):
    def operation(self):
        return 'logic operation from productB1'

    def another_operation(self, concrete: ProductA):
        return f"from A class's method {concrete.operation()}"


class ConcreteProductB2(ProductB):
    def operation(self):
        return 'logic operation from productB2'

    def another_operation(self, concrete: ProductA):
        """
        在B的基础上调用A的方法
        这样不会牵一发而动全身
        """
        return f"from A class's method by b call ---> {concrete.operation()}"


if __name__ == '__main__':
    """
    client
    用途：自定义插件
    """
    productA = ConcreteAbstractFactoryA().do_product_a()
    productB = ConcreteAbstractFactoryB().do_product_b()
    result = productB.another_operation(productA)
    print(result)
