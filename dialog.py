# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(QtWidgets.QWidget):
    def setupUi(self, Dialog, status):
        self.status = status
        Dialog.setObjectName("Dialog")
        Dialog.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        if status == 'info':
            Dialog.resize(300, 200)
        else:
            Dialog.resize(240, 135)
        Dialog.setFixedSize(Dialog.width(), Dialog.height())
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setWindowFlags(QtCore.Qt.CustomizeWindowHint
                              | QtCore.Qt.WindowCloseButtonHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_icon = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label_icon.sizePolicy().hasHeightForWidth())
        self.label_icon.setSizePolicy(sizePolicy)
        if status == 'info':
            self.label_icon.setMinimumSize(QtCore.QSize(60, 60))
            self.label_icon.setMaximumSize(QtCore.QSize(60, 60))
        else:
            self.label_icon.setMinimumSize(QtCore.QSize(40, 40))
            self.label_icon.setMaximumSize(QtCore.QSize(40, 40))
        self.label_icon.setText("")
        self.label_icon.setAlignment(QtCore.Qt.AlignCenter)
        self.label_icon.setObjectName("label_icon")
        self.horizontalLayout_2.addWidget(self.label_icon)
        space_width = 0
        if status == 'info':
            space_width = 20
        else:
            space_width = 10
        spacerItem = QtWidgets.QSpacerItem(space_width, 40,
                                           QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        self.horizontalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setDefault(False)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(Dialog.close)
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        if status == 'success':
            self.label.setText("导入成功！")
            self.label_icon.setStyleSheet(
                "#label_icon{border-image:url(./icons/success.png);}")
        elif status == 'warning':
            self.label.setText("已导入课程，更新数据文件失败！\n请检查数据库文件读写权限！")
            self.label_icon.setStyleSheet(
                "#label_icon{border-image:url(./icons/warning.png);}")
        elif status == 'info':
            self.label.setText(
                "迷你课程表开发者：\n刘怿睿\t2019210367\n杨　亮\t2019210362\n黄诗扬\t2019210374\n郭佩圣\t2019210375\n李硕\t2019210376"
            )
            self.label_icon.setStyleSheet(
                "#label_icon{border-image:url(./icons/warning.png);}")
            font = QtGui.QFont()
            font.setFamily("微软雅黑 Light")
            font.setPointSize(10)
            self.label.setFont(font)
        elif status == 'fail':
            self.label.setText("导入失败，请重试！")
            self.label_icon.setStyleSheet(
                "#label_icon{border-image:url(./icons/fail.png);}")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        if self.status == 'info':
            Dialog.setWindowTitle(_translate("Dialog", " 关于"))
            Dialog.setWindowIcon(QtGui.QIcon("./icons/warning.png"))
        else:
            Dialog.setWindowTitle(_translate("Dialog", "导入结果"))
            Dialog.setWindowIcon(QtGui.QIcon("./icons/icon.ico"))
        self.pushButton.setText(_translate("Dialog", "确定"))
