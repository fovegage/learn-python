# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 15:57
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : SQLAlchemy_stu.py
# @Software: PyCharm

# 即ORM模型

# 导入:
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:
class User(Base):
    # 表的名字:
    __tablename__ = 'user'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

# 初始化数据库连接:
engine = create_engine('Mysql://root:416798@localhost/test')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)