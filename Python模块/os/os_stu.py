# -*- coding: utf-8 -*-
# @Time    : 2019/4/3 17:32
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : os_stu.py
# @Software: PyCharm

import os

'DirEntry', 'F_OK', 'MutableMapping', 'O_APPEND', 'O_BINARY', \
'O_CREAT', 'O_EXCL', 'O_NOINHERIT', 'O_RANDOM', 'O_RDONLY', 'O_RDWR',\
'O_SEQUENTIAL', 'O_SHORT_LIVED', 'O_TEMPORARY', 'O_TEXT', 'O_TRUNC', \
'O_WRONLY', 'P_DETACH', 'P_NOWAIT', 'P_NOWAITO', 'P_OVERLAY', 'P_WAIT',\
'PathLike', 'R_OK', 'SEEK_CUR', 'SEEK_END', 'SEEK_SET', 'TMP_MAX', 'W_OK',\
'X_OK',  'abc', 'abort', 'access', 'altsep', 'chdir', 'chmod', 'close', \
'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull', \
'dup', 'dup2', 'environ', 'errno', 'error', 'execl', 'execle', 'execlp', 'execlpe',\
'execv', 'execve', 'execvp', 'execvpe', 'extsep', 'fdopen', 'fsdecode', 'fsencode', \
'fspath', 'fstat', 'fsync', 'ftruncate', 'get_exec_path', 'get_handle_inheritable', \
'get_inheritable', 'get_terminal_size', 'getcwd', 'getcwdb', 'getenv', 'getlogin', \
'getpid', 'getppid', 'isatty', 'kill', 'linesep', 'link', 'listdir', 'lseek',\
'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir', 'path', 'pathsep', \
'pipe', 'popen', 'putenv', 'read', 'readlink', 'remove', 'removedirs', \
'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_handle_inheritable', \
'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile',\
'stat', 'stat_float_times', 'stat_result', 'statvfs_result', 'strerror',\
'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids', 'supports_fd',\
'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', \
'times', 'times_result', 'truncate', 'umask', 'uname_result', 'unlink', 'urandom', \
'utime', 'waitpid', 'walk', 'write'



print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(dir(os.path))

os.access()