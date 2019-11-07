#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-11-07 09:39
# @Author  : Lqq/linqingqing
# @Site    : 
# @File    : run.py
# @Software: PyCharm

import sys
import os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
import traceback
import requests
import time

from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtWidgets
from view.chinaz import Ui_Widget
from util.database import Db
from util.web_chinaz import WebUrl


class Worker(QtCore.QThread):
    sig = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0

    def __del__(self):
        self.working = False
        self.wait()


    def run(self):
        while self.working == True:
            for page in range(0, 1921):
                self.sig.emit(page)
                print("run\n")
                time.sleep(1)

class Combosel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Combosel, self).__init__(parent)

        self.ui_sel = Ui_Widget()
        self.ui_sel.setupUi(self)

        # 清理结果集
        self.ui_sel.result.clear()

        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sig.connect(self.get_data)

        # 连接自己的槽函数
        self.ui_sel.okButton.clicked.connect(self.onActivatedpushButton)



    # 获取网页数据
    def get_data(self,page):
        print(page+"\n")
        try:
            if page <= 1:
                path = WebUrl().url + "/index.html"
            else:
                path = WebUrl().url + "/index_" + str(page) + ".html"

            response = requests.get(path, headers=WebUrl().headers)
            response.encoding = 'utf-8'
            data = response.content
            soup = bs(data, 'html.parser')
            divlist = soup.find_all("div", attrs={"class": "CentTxt"})
            for value in divlist:
                title = value.find("a", attrs={'class': 'pr10 fz14'}).get_text()
                domain = value.find("", attrs={'class': 'col-gray'}).get_text()

                host = self.ui_sel.host.text()
                port = self.ui_sel.port.text()
                user = self.ui_sel.user.text()
                passwd = self.ui_sel.passwd.text()
                db = self.ui_sel.db.text()
                charset = self.ui_sel.charset.text()
                Db(host, port, user, passwd, db, charset).insert_domain(title, domain)

                self.ui_sel.result.insertPlainText("标题：" + title + ", 域名：" + domain + "数据添加成功\n")
                text_cur = self.ui_sel.result.textCursor().End
                self.ui_sel.result.moveCursor(text_cur)
        except:
            traceback.print_exc()

    # 点击
    def onActivatedpushButton(self):
        try:
            self.thread.start()
        except:
            traceback.print_exc()

if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        Appcombosel = Combosel()
        Appcombosel.show()
        sys.exit(app.exec_())
    except:
        traceback.print_exc()
