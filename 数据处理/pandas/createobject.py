# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 14:33
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : createobject.py
# @Software: PyCharm

import pandas as pd
import numpy as np

# 创建series index 修改序号  dtype 指定数据类型
s = pd.Series([1, 2, 3, 5], index=list('abcd'))
print(s)

# 创建日期数组
dates = pd.date_range('20190301', periods=6)
print(dates)

# 创建二维数据表  index columns 不指定默认按 0-n
f = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print(f)

# 字典对象
f1 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20190301'),
    'C': pd.Series(1, index=np.arange(4), dtype='float32'),
    'D': np.array([3] * 3),
    'E': pd.Categorical(['Python', 'C', 'C++']),
    'F': 'foo'

}, index=np.arange(3))
print(f1)

# 查看数据类型
print(f1.dtypes)

# 查看数据
print(f1.head(2))
print(f1.tail(1))

# 显示列 索引 值
print(f1.values)
print(f1.items)
print(f.index)
print(f.columns)

# 对数据进行统计  只对数据列进行
print(f1.describe())

# 转置
print(f1.T)

# 排序
print(f.sort_index(axis=1))

# 按列
print(f.sort_values(by='D'))

# 通过标签取值
print(f1['E'])  # 按 columns
print(f1[0:1])  # 按行
print(f['20190301': '20190304'])  # 按 index
print(f.loc[:, ['A', 'B']])  # 钱切片 后列
print(f.loc['20190302':'20190304', ['A', 'B']])
print(f.loc['20190305', ['A', 'B']])  # index columns
print(f.loc[dates[0]])# 获取一个坐标值

# 通过位置取值
print(f.iloc[3])  # 列
print(f.iloc[0:4, 3: 4])  # 行 列
print(f.iloc[[1, 2, 4], [1, 3]])  # 获取指定行和列
print(f.iloc[1: 2, 3: 4])
print(f.iloc[1:2, :])
print(f.iloc[:, 3:4])
print(f.iloc[1, 1])  # 获取单元格值 特定值
print(f.iat[1, 1])  # 获取单元格值 特定值

# 布尔suoyin
print(f[f.A > 0])
print(f[f > 0])  # 小于零的数据显示NaN

# 过滤
print(f1[f1['E'].isin(['C'])])

# 设置新列
print(f)
g = pd.Series(np.arange(6), index=pd.date_range('20190301', periods=6))
f['G'] = g
print(f)
# 设置新值
f.iat[1, 2] = 882
print(f)

# 标签换值
f.loc[:, 'D'] = np.array([6] * len(f))
print(f)

# 缺值填充
miss = f[f > 0]
print(miss)
print(miss.dropna(how='any'))
fill = miss.fillna(value=999)
print(fill)  # 不可变

# 布尔填充 NaN 为False
print(pd.isnull(miss))

# 平均值
print(f.mean())  # 按列计算
print(f.mean(1))

dates = pd.date_range('20190301', periods=6)
s1 = pd.Series([1, 3, 5, 6, np.NAN, 7], index=dates).shift(3)
print(s1)
print(f)
print(f.sub(s1, axis='index'))

print(f.apply(np.cumsum))  # 运用 cumsum进行计算
f3 = pd.DataFrame([[1, 2, 99], [4, 5, 6], [3, 5, 7]])
print(f3)
print(f3.apply(lambda x: x.max() - x.min()))
