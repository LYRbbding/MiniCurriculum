import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent_addr=None, parent=None):
        super(TrayIcon, self).__init__(parent)
        self.parent_addr = parent_addr
        self.showMenu()
        self.activated.connect(self.iconClied)
        self.setIcon(QIcon("./icons/icon.ico"))
        self.icon = self.MessageIcon()

    def showMenu(self):
        self.menu = QMenu()
        self.showAction = QAction("显示/隐藏窗口",
                                  self,
                                  triggered=self.change_windows)
        self.quitAction = QAction("退出", self, triggered=self.quitProgram)
        self.menu.addAction(self.showAction)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

    def iconClied(self, reason):
        #控制主界面是否显示，鼠标点击icon传递的信号会带有一个整形的值
        #1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
        if reason == 2 or reason == 3:
            if self.parent().isVisible():
                self.parent().hide()
            else:
                self.parent().show()
                self.parent().raise_()

    def show_toast(self, title="迷你课程表", desc="这是程序的上课提醒功能"):
        self.showMessage(title, desc, self.icon)

    def change_windows(self):
        if self.parent().isVisible():
            self.parent().hide()
        else:
            self.parent().show()
            self.parent().raise_()

    def quitProgram(self):
        self.setVisible(False)
        self.parent_addr.exit_program()