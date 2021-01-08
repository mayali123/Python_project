# -*- coding: UTF-8 -*-
# @Time :  16:21
# @Author :mayali123
# @File : win.py
# @Software : PyCharm

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialog, QApplication, QLabel


class Search(QDialog):
    # 替换的信号
    sreachmsg = pyqtSignal(str)
    def __init__(self ):
        super(Search, self).__init__()
        self.newWindowUI()
        self.connect()
    def newWindowUI(self):
        self.setWindowTitle("查找")
        self.setWindowIcon(QIcon("./Resources/12.jpg"))
        self.setFixedSize(600, 180)
        #
        self.label = QLabel("查找内容：",self)
        self.label.setGeometry(QtCore.QRect(120, 40, 81, 31))
        #
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(200, 40, 241, 31))

        # 取消和 查找的按钮
        self.pushButton = QtWidgets.QPushButton("查找",self)
        self.pushButton.setGeometry(QtCore.QRect(80, 120, 92, 28))

        self.pushButton_2 = QtWidgets.QPushButton("取消",self)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 120, 92, 28))

    def connect(self):
        self.pushButton.clicked.connect(lambda :self.sreachmsg.emit(self.lineEdit.text()))
        self.pushButton_2.clicked.connect(lambda :self.close())

class Replace(Search):
    # 替换 的 信号
    replacemsg = pyqtSignal(str,str)

    def __init__(self):
        super(Replace, self).__init__()
        self.newWindowUI()
        self.connect()
        self.Updata()
    def Updata(self):
        self.setWindowTitle("替换")
        # self.label.clear()
        # self.label.setText("")
        # 替换为
        self.label1 = QLabel("替换为：", self)
        self.label1.setGeometry(QtCore.QRect(120, 75, 81, 31))

        # 输入 替换为
        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(200, 75, 241, 31))

        self.pushButton.setText("替换")

    def connect(self):
        self.pushButton.clicked.connect(lambda: self.replacemsg.emit(self.lineEdit.text(),  self.lineEdit1.text()))
        self.pushButton_2.clicked.connect(lambda: self.close())

# 调试 使用
if __name__ == '__main__':
    app = QApplication(sys.argv)
    sec = Replace()
    sec.show()
    sec.exec_()
    sys.exit(app.exec_())