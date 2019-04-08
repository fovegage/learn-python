# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 11:44
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : path_stu.py
# @Software: PyCharm

import os

# os.path.join	连接目录与文件名
# os.path.split	分割文件名与目录
# os.path.abspath	获取绝对路径
# os.path.dirname	获取路径
# os.path.basename	获取文件名或文件夹名
# os.path.splitext	分离文件名与扩展名
# os.path.isfile	判断给出的路径是否是一个文件
# os.path.isdir	判断给出的路径是否是一个目录

'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', \
'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', \
'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', \
'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', \
'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', \
'splitext', 'splitunc', 'stat', 'supports_unicode_filenames', 'sys'

################################################################################
# 变量系列
print(os.path.altsep)  # .. 上级
print(os.path.curdir)  # .
print(os.path.extsep)  # .
print(os.path.sep)  # \\
print(os.path.altsep)  # /
print(os.path.pathsep)  # ;
print(os.path.defpath)  # .;C:\\bin

#############################################################################
# 文件/目录系列
# 不会检验是否存在真实路径  \love 和 love  都是输出  E:\love
# join 加参数 拼接返回上一级
# 不断调用 diranme 也可以 返回上一级
print(os.path.join('E:\\', '\love', os.path.altsep))
print(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# 返回路径
print(__file__)  # 返回当前文件所在的目录，包括文件名  将返回 linux的 / 作为分割
print(os.path.abspath(__file__))  # windows 形式 \  由平台觉得是 \ /  linux /  windows \

# 拆分文件
print(os.path.basename(__file__))  # 返回文件名称  spilt[1]
print(os.path.dirname(__file__))  # 返回当前文件所在的目录，不包括文件名 spilt[0]
print(os.path.split(__file__))  # 元组返回上面的

# ('F:/pystudy/learn-python3/Python模块/os/path_stu', '.py')
print(os.path.splitext(__file__))

# 返回共有最长的路径
print(os.path.commonpath(['E:\\a', 'E:\\a\\c']))
print(os.path.commonprefix(['E:\\a', 'E:\\a\\c']))

# 判断路径是否真实存在
print(os.path.exists('F:\\work'))  # 路径存在则返回True,路径损坏返回False
print(os.path.lexists('F:\\w'))  # 路径存在则返回True,路径损坏也返回True
####################################################
# is系列
# 判断是否是路径  会校验真实性
print(os.path.isdir('F:\\'))

# 判断是否为文件
print(os.path.isfile(__file__))

# 判断路径是否为链接  即快捷方式
print(os.path.islink(__file__))

# 判断是否为挂载点
print(os.path.ismount('F:\\'))

# 判断是否为绝对路径
print(os.path.isabs(__file__))

#####################################################
print(os.path.expanduser('F:\\'))  # 把path中包含的"~"和"~user"转换成用户目录
print(os.path.expandvars(__file__))  # 根据环境变量的值替换path中包含的”$name”和”${name}”

#####################################################
# 时间大小类
print(os.path.getsize(__file__))  # kb
print(os.path.getctime(__file__))  # time.time()  创建时间
print(os.path.getatime(__file__))  # 最近访问时间
print(os.path.getmtime(__file__))  # 最近修改时间

####################################################
print(os.path.normcase('F:\\WORK'))  # 转小写
print(os.path.normpath(__file__))  # 规范路径  消除双斜线 \

###################################################
print(os.path.realpath(__file__))  # 返回path的真实路径
print(os.path.relpath(__file__, 'os'))  # 指定位置 输出相对路径

##################################################
print(os.path.samefile('F:\\test.txt', 'F:\\test.txt'))  # 判断目录或文件是否在同一级 校验是否存在
f = os.open('F:\\test.txt', os.O_RDWR | os.O_CREAT)
print(os.path.sameopenfile(f, f)) # 判断fp1和fp2是否指向同一文件
# print(os.path.samestat())


####################################################
# 分割系列
print(os.path.splitext(__file__))   # 分割出类似于 .py
print(os.path.split(__file__))   # 分割 目录和文件
print(os.path.splitunc(__file__))  # 把路径分割为加载点与文件
print(os.path.splitdrive(__file__)) # windows 盘符和 文件目录分开

