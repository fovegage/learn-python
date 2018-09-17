# -*- coding: utf-8 -*-
# @Time    : 2018/9/17 10:35
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : pico_test.py
# @Software: PyCharm


import os
from time import sleep
import pexpect
import sys
from xlwt import *


class PicoTest():

    def __init__(self, mastertest, testtime):
        self.mastertest = mastertest
        self.testtime = testtime
        self.masterpath = "G:\\test\\" + self.mastertest
        self.dot = '.'

    def CreateFile(self):
        if "test" in os.listdir('G:\\'):
            if self.mastertest not in os.listdir("G:\\test"):
                os.mkdir(self.masterpath)
                os.mkdir(self.masterpath + "\\" + self.mastertest + self.dot + str(1))
            else:
                self.num = int(os.listdir(self.masterpath)[-1].split(".")[1])
                os.mkdir(self.masterpath + "\\" + self.mastertest + self.dot + str(self.num + 1))
        else:
            os.mkdir("G:\\test")
            if self.mastertest not in os.listdir("G:\\test"):
                os.mkdir(self.masterpath)
                os.mkdir(self.masterpath + "\\" + self.mastertest + self.dot + str(1))
            else:
                self.num = int(os.listdir(self.masterpath)[-1].split(".")[1])
                os.mkdir(self.masterpath + "\\" + self.mastertest + self.dot + str(self.num + 1))

    def TestStop(self):
        sleep(self.testtime)
        child = pexpect.spawn('ssh root@172.16.16.103')
        child.logfile = sys.stdout
        child.expect('password:')
        child.sendline('root123')
        child.expect('root*')
        child.sendline('reboot \n')


    def CopyLog(self):
        self.path = self.masterpath + "\\" + self.mastertest + self.dot + str(self.num + 1)
        os.chdir(self.path)
        # os.system("tar -cvf {}.tar.gz /NbTest/log/./*".format(self.path.split("\\")[3]))


    def GenResult(self):
        # os.system("cp -r /NbTest/result/result.txt /{}".format(self.path))
        print(self.path)

    def ConfigFile(self):
        return '"测试例", {}, "测试时间", {}'.format(self.mastertest, self.testtime)

    def GenConfig(self):
        file = Workbook(encoding='utf-8')
        table = file.add_sheet(self.mastertest)
        data = {
            self.num: [self.ConfigFile()],
        }
        ldata = []
        num = [a for a in data]
        num.sort()
        for x in num:
            t = [int(x)]
            for a in data[x]:
                t.append(a)
            ldata.append(t)

        for i, p in enumerate(ldata):
            for j, q in enumerate(p):
                table.write(i, j, q)
        file.save('G:\\{}.xlsx'.format(self.mastertest))

    def Clean(self):
        os.system("rm -rf /NbTest/log/./*")
        os.system("rm -rf /NbTest/result/result.txt")

if __name__ == '__main__':
    pico = PicoTest('test5', 30)
    pico.CreateFile()
    # pico.TestStop()
    # pico.CopyLog()
    # pico.GenResult()
    pico.GenConfig()
