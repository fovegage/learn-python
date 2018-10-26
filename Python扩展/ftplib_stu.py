# -*- coding: utf-8 -*-
# @Time    : 2018/10/26 10:36
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : ftplib_stu.py
# @Software: PyCharm

from ftplib import FTP

class VerfyInfo:
    def __init__(self):
        self.ip = '172.16.16.103'
        self.username = 'root'
        self.passwoed = 'root123'


    def instance(self):
        self.f = FTP(self.ip)
        self.f.login(self.username, self.passwoed)

    def upload(self):
        self.instance()
        print(self.f.cwd('/root/'))
        file_remote = 'ftp_upload.txt'
        file_local = 'F:\\a.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'rb')
        self.f.storbinary('STOR ' + file_remote, fp, bufsize)
        fp.close()

    def download(self):
        file_remote = '1.txt'
        file_local = 'D:\\test_data\\ftp_download.txt'
        bufsize = 1024  # 设置缓冲器大小
        fp = open(file_local, 'wb')
        self.f.retrbinary('RETR %s' % file_remote, fp.write, bufsize)
        fp.close()


VerfyInfo().upload()








