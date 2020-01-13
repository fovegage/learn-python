# https://www.the5fire.com/django-metaclass-compatibility.html
# https://www.ojit.com/article/82155
# https://www.cnblogs.com/ajianbeyourself/p/4052084.html
# https://www.cnblogs.com/zhaoshizi/p/9180886.html
# https://segmentfault.com/a/1190000012530796
# https://blog.csdn.net/dashoumeixi/article/details/80772832
# https://blog.csdn.net/liuyuan_jq/article/details/69608960

class ModelBase(type):
    def __new__(cls, name, bases, attrs):
        print(cls)
        return type.__new__(cls, name, bases, attrs)


class metaclass(ModelBase):
    def __new__(cls, name, this_bases, d):
        return ModelBase(name, (), d)  # 之前通过参数传递过来的``*bases``我们先去掉 - by the5fire


####
# 元类不会实例化，只要一个非元类继承才会进行实例化
# 这点很好理解  type(classname, parent_classname, attrs)
# 其中parent_classname 是一个元组 若为空的时候，就会隐式的继承object
# 但是在python中最后的老大哥是 type  但是type 并不会进行实例化
# 这是鬼叔设计的 就这样 因为不可能无限制的递归下去  当然type 的__class__ 不管进行几次
# 都是 type
# 工厂方法 with_metaclass 在类内已经完成了对象继承和属性赋值  外部 type.__new(cls, classname, parent_classname, attrs)
# cls 表示哪个类  他是type 的子类或type类  他django 的这个列子中 他就表示在Model类中
# 因此 model.__mro__  只要 ModelBase(继承类) 和 object(隐式继承)
# djnago2.0 以下的版本是为了兼容py2 和py3 利用python 提供的six.with_metaclass 进行的转化
# python2 和 python 3 的 元类声明不一样

####
MetaClassForInherit = type.__new__(metaclass, 'temporary_class', (), {})

# class Model(MetaClassForInherit):
#     pass
