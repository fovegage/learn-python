# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 11:56
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : ssh.py
# @Software: PyCharm

import pexpect
import sys
from  pexpect import pxssh
child = pexpect.spawn('ssh root@172.16.16.103')
child.logfile = sys.stdout
child.expect('password:')
child.sendline('root123')
child.expect('root*')
child.sendline('ls ./')
child.interact()

