# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 17:16
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : mysql_stu.py
# @Software: PyCharm
import pymysql




def query(sql):
    db = pymysql.connect("localhost", "root", "416798", "test")
    cursor = db.cursor()
    sql = sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    db.close()

print(query('select * from user'))



class Query():
    def __init__(self, sql, host, username, password, database):
        self.sql

