# -*- coding: utf-8 -*-
# @Time    : 2018/11/8 9:51
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : file.py
# @Software: PyCharm

# r / w / a  读或写  覆盖
# r+ / w+ / a+  读写
# rb / wb / ab  二进制读或写  覆盖
# rb+ / wb+ / ab+  读写



# 读read
f = open('E:\\test.txt', 'r')
content = f.read()
print(content)
print(f.name, f.mode)  # 文件名  模式
f.close()
print("*"*100)

# write()  w不可以写中文
f = open('E:\\test.txt', 'w+')
f.write('dlllllllllllllllllllldd多对多')
f.close()

# 读readline()  一次读一行
f = open('E:\\test.txt', 'r')
content = f.readline()
print(content)
f.close()
print("*"*100)

# 读readlines()  全部读出  列表封装
f = open('E:\\test.txt', 'r')
content = f.readlines()
print(content)
f.close()
print("*"*100)

# seek() / tell()
f = open('E:\\test.txt', 'r')
content = f.readline()
print(content)
f.seek(1, 0)   # offset 需要移动的字节数   whence： 0 开头 1 当前 2 末尾
print(f.tell())  # 获取指针位置
content = f.readline()
print(content)
f.close()
print("-"*100)

# truncate()  必须有写属性   因为截取删除
# f = open('E:\\test.txt', 'r+')
# content = f.read()
# print(content)
# f.truncate(8)
# f.close()
