# -*- coding: UTF-8 -*-
# @Time :  14:37
# @Author :mayali123
# @File : ReadFile.py
# @Software : PyCharm
import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon, QColor, QFont, QPalette, QTextDocument
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QLabel, QFontDialog, QColorDialog, QFileDialog, \
     QMessageBox
import chardet
from PyQt5 import QtCore, QtWidgets
import txt

class Read_FileWin(QMainWindow):
    def __init__(self,parent =None):
        super(Read_FileWin,self).__init__()
        # 显示
        self.setupUi()
        # 链接函数
        self.connect()
        # 初始化 一些 变量
        self.font = QFont()
        self.color = QColor()
        self.filename = None
        self.encode = "utf-8"
        self.IsSave = True
    # 显示
    def setupUi(self):
        # 设置 名字
        self.setWindowTitle("文件读取器")
        # 设置窗口的大小
        self.setFixedSize(800, 600)

        # 设置 窗口的 图标
        self.setWindowIcon(QIcon("./Resources/12.jpg"))

        # 行 编辑框
        self.lineEdit = QtWidgets.QLineEdit(self)

        # QRect ( int left, int top, int width, int height )
        self.lineEdit.setGeometry(QtCore.QRect(10, 35, 641, 31))

        # 按钮
        self.pushButton = QtWidgets.QPushButton("选择文件",self)
        self.pushButton.setGeometry(QtCore.QRect(680, 35, 92, 28))

        # 菜单栏
        self.bar = self.menuBar()


        # 文件 菜单
        self.menuFile = self.bar.addMenu("文件")

        # 新建
        self.actionNew = self.menuFile.addAction("新建")
        # 打开
        self.actionOpen = self.menuFile.addAction("打开 Ctrl+o")
        # 保存
        self.actionSave = self.menuFile.addAction("保存 Ctrl+s")
        # 另存为
        self.actionOtherSave = self.menuFile.addAction("另存为")
        # 退出
        self.actionQuit = self.menuFile.addAction("退出")


        # 格式 菜单
        self.menuFormat = self.bar.addMenu("格式")

        # 设置颜色
        self.actionSet = self.menuFormat.addAction("设置颜色")
        # 设置字体
        self.actionSet_2 = self.menuFormat.addAction("设置字体")


        # 查看 菜单
        self.menuLook = self.bar.addMenu("查看")

        self.actionUp = self.menuLook.addAction("放大 Ctrl+加号")
        self.actionDown = self.menuLook.addAction("缩小 Ctrl+减号")
        self.actionSearch = self.menuLook.addAction("查找")
        self.actionReplace = self.menuLook.addAction("放大 Ctrl+加号")

        #  添加 菜单栏
        self.setMenuBar(self.bar)
        # 状态栏
        self.statusBar = QtWidgets.QStatusBar(self)

        # 添加 状态栏
        self.setStatusBar(self.statusBar)

        # num 是显示字数的
        self.text_num = QLabel(self)
        # text_encode 显示 编码的
        self.text_encode = QLabel(self)
        # text_IsSave 是否保存
        self.text_IsSave = QLabel(self)

        # 添加的状态栏
        self.statusBar.addWidget(self.text_num)
        self.statusBar.addWidget(self.text_IsSave)
        self.statusBar.addPermanentWidget(self.text_encode)

        # 设置初始值
        self.text_num.setText("字数0")
        self.text_IsSave.setText("已保存")
        self.text_encode.setText("编码:utf-8")

        # 文本框
        self.text = MyTextEdit(self)
        self.text.move(0, self.lineEdit.height() + 50)

        # 设置 文本框的大小
        self.text.resize(self.width(),
                         self.height() - self.statusBar.height() - self.lineEdit.height() - 50)

    # 链接 槽 和 信号
    def connect(self):
        # 退出 和 Quit 链接在一起
        self.actionQuit.triggered.connect(lambda:self.close())
        # 菜单栏的 打开 和 OpenFile 函数 链接在一起
        self.actionOpen.triggered.connect(self.OpenFile)
        # 保存 和 保存函数链接在一起
        self.actionSave.triggered.connect(self.SaveFile)
        # 另保存
        self.actionOtherSave.triggered.connect(self.SaveOtherFile)
        # 打开文件 按钮 和 OpenFile 函数 链接在一起
        self.pushButton.clicked.connect(self.OpenFile)


        # 设置 字的颜色
        self.actionSet.triggered.connect(self.SetColor)
        # 设置 字体
        self.actionSet_2.triggered.connect(self.SetFont)


        # 放大
        self.actionUp.triggered.connect(lambda :self.addDown(True))
        # 缩小
        self.actionDown.triggered.connect(lambda: self.addDown(False))
        # 查找
        self.actionSearch.triggered.connect(self.Search)
        # 替换
        self.actionReplace.triggered.connect(self.Replace)


        # 信号 和 槽 链接 起来
        self.text.savemeg.connect(self.SaveFile)
        self.text.openmeg.connect(self.OpenFile)
        self.text.addDown.connect(self.addDown)
        self.text.textChanged.connect(self.TextChanged)

    # 打开文件
    def OpenFile(self):
        print("打开")
        self.IsSave = True
        # 打开 文件对话框
        self.filename, ok = QFileDialog.getOpenFileName(None, "打开文件", "/", "(*.txt)")
        if ok:
            print(self.filename)
            # 将文件路径 添加到 lineEdit 中
            self.lineEdit.setText(self.filename)
            self.ReadFile()
        else:
            print("未选择文件")

    # 将文件内容写 到 文本框中
    def ReadFile(self):
        if self.filename != None:
            # 清屏
            self.text.clear()
            file = open(self.filename, "rb")
            # 解决 编码 问题
            self.encode = chardet.detect(file.readline())["encoding"]
            self.text_encode.setText("编码%s"% self.encode)
            print(self.encode)
            file.close()
            # 打开文件
            file = open(self.filename, "r", encoding=self.encode)
            # 设置 字体和颜色
            self.text.setFont(self.font)
            self.text.setTextColor(self.color)

            num = 0
            for i in file:
                num += self.WordNumber(i)
                self.text.append(i.replace("\n", ""))
            self.text_num.setText("字数%d" % num)

    # 设置字体
    def SetFont(self):
        self.font, ok = QFontDialog.getFont(None)
        self.ReadFile()

    # 设置颜色
    def SetColor(self):
        self.color = QColorDialog.getColor(QColor(255, 0, 0), None)
        self.ReadFile()

    # 当文本框有变化时
    def TextChanged(self):
        self.IsSave = False
        self.text_IsSave.setText("未保存")
        data = self.text.toPlainText()
        num = self.WordNumber(data)
        self.text_num.setText("数字%d" % num)

    # 保存文件
    def SaveFile(self):
        self.IsSave = True
        # 如果 文件名为 None
        if self.filename == None:
            self.filename, _ = QFileDialog.getSaveFileName(None, "新建", "./新建文本文件", "(*.txt)")

        # 如果是 ascii 的话 将其 变成 utf-8 就可以 保存中文了
        if self.encode == "ascii":
            self.encode = "utf-8"

        file = open(self.filename, "w", encoding=self.encode)
        # 得到 文本编辑框的文字
        data = self.text.toPlainText()
        file.write(data)
        file.close()

        # 显示 已保存
        self.text_IsSave.setText("已保存")
        # 重新设置 一下 文件路径
        self.lineEdit.setText(self.filename)

    # 另存为
    def SaveOtherFile(self):
        self.IsSave = True
        self.OtherFileName,ok = QFileDialog.getSaveFileName(None, "新建", "./新建文本文件", "(*.txt)")
        if ok:
            # 如果是 ascii 的话 将其 变成 utf-8 就可以 保存中文了
            if self.encode == "ascii":
                self.encode = "utf-8"
            file = open(self.OtherFileName, "w", encoding=self.encode)
            data = self.text.toPlainText()
            file.write(data)
            file.close()
            # 如果之前的 文件名为 None
            # if self.filename == None:
            #     self.filename = self.OtherFileName
            #     self.lineEdit.setText(self.OtherFileName)

    # 发大 or 缩小
    def addDown(self,IsUpOrDown):
        # 如果是放大
        if IsUpOrDown:
            self.font.setPointSize(self.font.pointSize() + 5) # 将字变大
        else:
            self.font.setPointSize(self.font.pointSize() - 5)  # 将字变小
        self.ReadFile()  # 再重新显示文字


    # 这个函数的大概意思是过掉开始的空格，然后如果33(!)<=p[i]的ASC码值<=125(})
    # 且  下一个不是在上面那个范围里面或是空格,则count++
    # 如果  33(!)<=p[i]的ASC码值<=125(}) 不满足 且 不是空格
    # 这个模仿WPS,试出来的，说多了都是泪(╥﹏╥)
    def WordNumber(self, p):
        p += '\0'
        i = 0
        count = 0
        while p[i] == ' ':
            i += 1
        while p[i] != '\0':
            if ord(p[i]) >= 33 and ord(p[i]) <= 125:
                if p[i + 1] == ' ' or not(ord(p[i + 1]) >= 33 and ord(p[i + 1]) <= 125):
                    count += 1
            elif p[i] != ' ':
                count += 1
            i += 1
        return count

    def Search(self):
        sec = txt.Ui_MainWindow()
        sec.show()
        # 链接 槽函数
        sec.sreachmsg.connect(self.SearchString)
        sec.exec_()

    # 查找 字符串 并 高亮
    def SearchString(self,st):
        # 参考 https://blog.csdn.net/Phr_Nick/article/details/51533453?spm=1001.2101.3001.4242
        if self.text.find(st, QTextDocument.FindBackward):
            palette = self.text.palette()
            palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
            self.text.setPalette(palette)
        else:
            QMessageBox.information(None,"查找", "找不到\"{}\"".format(st))

    # 替换
    def Replace(self):
        sec = txt.Replace()
        sec.show()
        sec.replacemsg.connect(self.ReplaceShow)
        sec.exec_()

    # 替换
    def ReplaceShow(self, st, to_st):
        data = self.text.toPlainText()
        data = data.replace(st, to_st)
        self.text.clear()
        self.text.append(data)

    # 重新 关闭 事件
    def closeEvent(self, QCloseEvent):
        print("进入closeEvent")
        if not self.IsSave:
            # 对话框
            choice = QMessageBox.question(None, "退出", "你想要将更改保存到{}吗?".format(self.filename), QMessageBox.Save|QMessageBox.No| QMessageBox.Cancel)
            if choice == QMessageBox.Save:
                self.SaveFile()
            elif choice == QMessageBox.No :
                self.close()
            elif choice == QMessageBox.Cancel:
                self.ignore()
        else:
            self.close()

class MyTextEdit(QTextEdit):
    #  信号函数
    # 打开文件 的 信号
    savemeg = pyqtSignal(object)
    # 放大 or 缩小的信号
    addDown = pyqtSignal(object)
    # 打开文件 的信号
    openmeg = pyqtSignal(object)

    # 重写 keyPressEvent
    def keyPressEvent(self, QKeyEvent):

        if QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and QKeyEvent.key() == QtCore.Qt.Key_S:
            print("按下 ctrl！！and save")
            self.savemeg.emit(None)
            print("save 成功！！")
        elif QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and QKeyEvent.key() == QtCore.Qt.Key_O:
            print("按下 ctrl！！and o")
            self.openmeg.emit(None)
            print("打开")
        elif QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and QKeyEvent.key() == QtCore.Qt.Key_Minus:
            print("按下 ctrl！！and -")
            self.addDown.emit(False)
            print("缩小")
        elif  QKeyEvent.modifiers() == QtCore.Qt.ControlModifier and QKeyEvent.key() == QtCore.Qt.Key_Equal:
            print("按下 ctrl！！and =")
            self.addDown.emit(True)
            print("放大")

        # 后面的事情 交给 父类
        super().keyPressEvent(QKeyEvent)

def main():
    app = QApplication(sys.argv)
    ui = Read_FileWin()
    ui.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()