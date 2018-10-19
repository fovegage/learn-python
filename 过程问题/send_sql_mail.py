# -*- coding: utf-8 -*-
# @Time    : 2018/10/18 16:25
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : send_sql_mail.py
# @Software: PyCharm
import tablib
import pymysql
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart

# 查询数据
def query(sql):
    db = pymysql.connect("localhost", "root", "416798", "hahaha")
    cursor = db.cursor()
    sql = sql
    try:
        cursor.execute(sql)
        return cursor.fetchall()
    except:
        print("Error: unable to fetch data")

    db.close()

# 导出到excel
def Export():
    sql = query('select GROUP_CONCAT(COLUMN_NAME) from information_schema.COLUMNS where table_name = "good" and table_schema ="hahaha";')[0]

    headers = str(sql[0]).split(',')
    data = query('select * from good')

    genexcel = tablib.Dataset(*data, headers=headers)
    with open('excel.xlsx', 'wb') as f:
        f.write(genexcel.xlsx)

# 发送邮件
def SendMail():

    _user = '602556194@qq.com'
    _pwd = "**************"
    _to = "sdgaozhe@163.com"

    msg = MIMEMultipart()
    body = MIMEText("数据库", 'HTML', 'utf-8')
    msg['Subject'] = Header("数据库", 'utf-8')
    msg['From'] = _user
    msg['To'] = _to

    msg.attach(body)

    # 添加附件
    att = MIMEText(open("F:\\pystudy\\learn-python3\\过程问题\\excel.xlsx", "rb").read(), "base64", "utf-8")  # 打开附件地址
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test.xlsx"'
    msg.attach(att)

    # 发送邮件
    s = smtplib.SMTP_SSL("smtp.qq.com")
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())

    s.quit()
    print("邮件发送成功")



if __name__ == '__main__':
    Export()
    SendMail()