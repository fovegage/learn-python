#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File:str_stu.py 
@Author:fovegage
@Contact:fovegage@gmail.com
@Created Time:2019/8/20 10:26   
@Version:1.0
'''

# 对于str类型我们仍然可以进行解压操作，这是Python可变数据类型所共有的特性
name = 'gage'
a, b, c, d = name
print(a, b, c, d)

# 集合str方法进行，我们只需要nobody、/var/empty、/usr/bin/false 三个数据
# 我们可以使用 *_ 占位符进行输出
path = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'

print(path.split(':'))

name, *_, path1, path2 = path.split(':')
print(name, path1, path2)
