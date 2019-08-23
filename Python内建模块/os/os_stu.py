# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 17:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_stu.py
# @Software: PyCharm

import os

'DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', \
'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR', \
'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', \
'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT', \
'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK', \
'X_OK', 'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', \
'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', \
'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe', \
'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', \
'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', \
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', \
'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek', \
'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', \
'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', \
'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', \
'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', \
'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror', \
'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd', \
'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', \
'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', \
'utime', 'waitpid', 'walk', 'write'

# 返回当前文件所在目录下的文件名
print(os.listdir())

# 如果允许访问返回 True , 否则返回False。 根据四种模式
# F_OK W_OK R_OK X_OK
f1 = os.access('F:\\test.txt', os.X_OK)
print(f1)

# getcwd 当前目录
print(os.getcwd())

# 切换目录
os.chdir('E:\\')
print(os.getcwd())

# 创建/删除目录
# os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以,
# 而且需要保证文件夹未被创建
os.mkdir('F:\\hello')
os.rmdir('F:\\hello')

# 重命名文件或目录
# os.rename('F:\\a.txt', 'F:\\h.txt')

# 删除文件
# os.remove('F:\\h.txt')

# 递归进行
# rename 不能修改 文件夹  renames 进行递归向上修改
# os.renames('F:\\test\\a.txt', 'F:\\test1\\b.txt')

# 递归进行  rmdir 只能删除一个非空的目录
os.chdir("F:\\test1\\")
print(os.listdir(os.getcwd()))
os.removedirs("F:\\test1\\test\\test")  # 单个删除不能加 \\   顶层 test1 不会被删除