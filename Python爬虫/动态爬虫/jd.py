# -*- coding: utf-8 -*-
# @Time    : 2018/11/9 22:11
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : jd.py
# @Software: PyCharm


from selenium import webdriver  # 选择要使用的浏览器
from selenium.webdriver.chrome.options import Options #chorm参数
from selenium.webdriver.common.keys import Keys
import time


class JD():
    def __init__(self, username, password):
        self.driver = webdriver.Chrome(executable_path='./chromedriver')
        elf.username = username
        self.password = password

    def login(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver.get('https://cart.jd.com/cart.action')
        self.driver.find_element_by_link_text('你好，请登录').click()
        self.driver.find_element_by_link_text('账户登录').click()
        self.driver.find_element_by_name('loginname').send_keys(self.username)
        self.driver.find_element_by_id('nloginpwd').send_keys(self.password)
        self.driver.find_element_by_id('loginsubmit').click()

        time.sleep(3)

        # self.driver.get("https://cart.jd.com/cart.action")
        # self.driver.find_element_by_link_text('去结算').click()
        # time.sleep(5)
        self.driver.close()

j = JD('sdgaozhe', '416798gao')
j.login()
