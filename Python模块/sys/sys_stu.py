# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 17:14
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : sys_stu.py
# @Software: PyCharm

# os.path 是一个模块，用来处理目录、路径相关的模块
# sys.path 是一个列表，返回解释器相关的目录列表、环境变量、注册表等初始化信息
'api_version', 'argv', 'base_exec_prefix', 'base_prefix', 'builtin_module_names', \
'byteorder', 'call_tracing', 'callstats', 'copyright', 'displayhook', 'dllhandle', \
'dont_write_bytecode', 'exc_info', 'excepthook', 'exec_prefix', 'executable', 'exit', \
'flags', 'float_info', 'float_repr_style', 'get_asyncgen_hooks', 'get_coroutine_wrapper',\
'getallocatedblocks', 'getcheckinterval', 'getdefaultencoding', 'getfilesystemencodeerrors',\
'getfilesystemencoding', 'getprofile', 'getrecursionlimit', 'getrefcount', 'getsizeof', \
'getswitchinterval', 'gettrace', 'getwindowsversion', 'hash_info', 'hexversion', 'implementation', \
'int_info', 'intern', 'is_finalizing', 'maxsize', 'maxunicode', 'meta_path', 'modules', 'path', 'path_hooks',\
'path_importer_cache', 'platform', 'prefix', 'set_asyncgen_hooks', 'set_coroutine_wrapper', 'setcheckinterval', \
'setprofile', 'setrecursionlimit', 'setswitchinterval', 'settrace', 'stderr', 'stdin', 'stdout', 'thread_info',\
'version', 'version_info', 'warnoptions', 'winver'
import sys

# 列表返回 [filename, param, ...]
# F:\pystudy\learn-python3\Python模块\sys>python3 sys_stu.py 543 878
# ['sys_stu.py', '543', '878']
print(sys.argv)  # 接受外界值

# exit()  用户主动退出主程序   正常为0  其他数值为异常  状态自定义

# def test_exit(value):
#     print(value)
#     sys.exit(0)
#
# try:
#     sys.exit(3333)
#
# except SystemExit as error:  # 注意这里 Python3 和 Python2 的区别
#     # print(error.args, error.code)
#     test_exit(error.code)

# sys.modules
# 是一个全局字典，该字典是python启动后就加载在内存中。
# 每当程序员导入新的模块，sys.modules将自动记录该模块。
# 当第二次再导入该模块时，python会直接到字典中查找，从而加快了程序运行的速度。
# 返回一个 dict  keys 模块名称  values 模块位置
print(sys.modules)

# Python 安装路径
print(sys.base_exec_prefix)

# Python 解释器路径
print(sys.executable)

# 所有Python 模块 非 from import 模块
print(sys.builtin_module_names)

# 解释器信息
print(sys.implementation)

# 返回操作系统
print(sys.platform)

# 返回字符集编码
print(sys.getdefaultencoding())

# # 捕捉系统异常信息
# print(sys.exc_info())
# types, value, back = sys.exc_info()
#
# # 打印异常
# sys.excepthook(types, value, back)

# 获取引用计数
print(sys.getrefcount(object))

# 获取Python版本
print(sys.version)

# 获取最大递归栈数
print(sys.getrecursionlimit())

# 设置最大递归栈数
sys.setrecursionlimit(2000)

# 获取线程切换间隔时间
print(sys.getswitchinterval())

# 设置线程切换间隔时间
sys.setswitchinterval(0.006)

