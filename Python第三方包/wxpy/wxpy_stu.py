# -*- coding: utf-8 -*-
# @Time    : 2018/11/21 16:49
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : wxpy_stu.py
# @Software: PyCharm
from wxpy import Bot
import schedule
import pymysql
import time
import random
from datetime import datetime


def query(sql):
    db = pymysql.connect("localhost", "root", "416798", "blog")
    cursor = db.cursor()
    sql = sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    db.close()

def dayNum():
    d1 = datetime.strptime('2018-07-11 17:41:20', '%Y-%m-%d %H:%M:%S')
    d2 = datetime.now()
    delta = d2 - d1
    return delta.days

def send():
    sql = 'select gonggao from blog_baseinfo'
    name = ['小可爱', '宝宝', '小菲菲']
    info = ['爸爸', 'Dad', '爹爹']
    message = query(sql)[0][0]
    bot = Bot(cache_path=True)
    # my_friend = bot.friends().search('白米饭er')[0]
    bot.file_helper.send(
        message+'~' + '\n'
        '{}今天是我们在一起的第{}天哟~'.format(random.choice(name), dayNum()) + '\n'
        '\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t来自{}的关爱~'.format(random.choice(info))
    )

schedule.every().day.at('22:31').do(send)

while True:
    schedule.run_pending()
    time.sleep(1)