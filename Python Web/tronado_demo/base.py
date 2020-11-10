# -*- coding: utf-8 -*-
# @Time    : 2018/12/18 18:02
# @Author  : fovegage
# @Email   : fovegage@gmail.com
# @File    : check.py
# @Software: PyCharm

from tornado import web, escape
# 主要模块

# web - FriendFeed 使用的基础 Web 框架，包含了 Tornado 的大多数重要的功能
# escape - XHTML, JSON, URL 的编码/解码方法
# database - 对 MySQLdb 的简单封装，使其更容易使用
# template - 基于 Python 的 web 模板系统
# httpclient - 非阻塞式 HTTP 客户端，它被设计用来和 web 及 httpserver 协同工作
# auth - 第三方认证的实现（包括 Google OpenID/OAuth、Facebook Platform、Yahoo BBAuth、FriendFeed OpenID/OAuth、Twitter OAuth）
# locale - 针对本地化和翻译的支持
# options - 命令行和配置文件解析工具，针对服务器环境做了优化

# 底层模块

# httpserver - 服务于 web 模块的一个非常简单的 HTTP 服务器的实现
# iostream - 对非阻塞式的 socket 的简单封装，以方便常用读写操作
# ioloop - 核心的 I/O 循环