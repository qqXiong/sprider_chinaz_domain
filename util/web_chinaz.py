#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 09:40
# @Author  : Lqq/linqingqing
# @Site    : 
# @File    : web_chinaz.py
# @Software: PyCharm

class WebUrl:
    def __init__(self):
        # 设置请求头，模拟浏览器访问
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        }
        self.url = 'https://top.chinaz.com/all/'

if __name__ == "__main__":
    WebUrl().get_web()