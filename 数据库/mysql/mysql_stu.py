# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 17:16
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : mysql_stu.py
# @Software: PyCharm
import pymysql
import configparser

def query(sql):
    """
    大批量插入，应该使用连接池
    注意MySQL maxclients 最大为 max_connections=1000;
    """
    db = pymysql.connect("localhost", "root", "416798Gao!", "test")
    print(id(db))
    cursor = db.cursor()
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        print(f"Error: unable to fetch data, {e}")

    db.close()


if __name__ == '__main__':
    for item in range(100):
        print(query('select * from student;'))
