# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from data import *
from shutil import copyfile
import sqlite3, os, sys, sip, time
import dialog, spirit, tray

class Ui_MainWindow(QtWidgets.QMainWindow):
    
    def setupUi(self, MainWindow):
        #托盘图标初始化
        self.TrayWidget = tray.TrayIcon(self, MainWindow)
        self.TrayWidget.show()
        
        #变量及地址初始化
        self.MainWindow = MainWindow
        self.WeekStart = 0
        self.WeekEnd = 15
        self.DateStart = 0
        self.DateEnd = 4
        self.SectionStart = 0
        self.SectionEnd = 13
        self.Classroom = ""
        self.Course= ""
        self.MainWindow = MainWindow
        
        #窗口基本参数设定
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setMinimumSize(QtCore.QSize(1024, 576))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        
        #窗口基本布局初始化
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        #程序窗口内标题初始化
        self.label_Title = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.label_Title.setFont(font)
        self.label_Title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Title.setObjectName("label_Title")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Title.sizePolicy().hasHeightForWidth())
        self.label_Title.setSizePolicy(sizePolicy)
        self.gridLayout.addWidget(self.label_Title, 0, 0, 1, 1)
        
        #程序功能区初始化
        #第一行水平布局
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        #周次部分
        self.label_Week = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Week.setFont(font)
        self.label_Week.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Week.setObjectName("label_Week")
        self.horizontalLayout.addWidget(self.label_Week)
        self.comboBox_WeekStart = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_WeekStart.setFont(font)
        self.comboBox_WeekStart.setObjectName("comboBox_WeekStart")
        self.horizontalLayout.addWidget(self.comboBox_WeekStart)
        self.label_Week2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Week2.sizePolicy().hasHeightForWidth())
        self.label_Week2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Week2.setFont(font)
        self.label_Week2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Week2.setObjectName("label_Week2")
        self.horizontalLayout.addWidget(self.label_Week2)
        self.comboBox_WeekEnd = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_WeekEnd.setFont(font)
        self.comboBox_WeekEnd.setObjectName("comboBox_WeekEnd")
        self.horizontalLayout.addWidget(self.comboBox_WeekEnd)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        #星期部分
        self.label_Date = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Date.setFont(font)
        self.label_Date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Date.setObjectName("label_Date")
        self.horizontalLayout.addWidget(self.label_Date)
        self.comboBox_DateStart = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_DateStart.setFont(font)
        self.comboBox_DateStart.setObjectName("comboBox_DateStart")
        self.horizontalLayout.addWidget(self.comboBox_DateStart)
        self.label_Date2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Date2.sizePolicy().hasHeightForWidth())
        self.label_Date2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Date2.setFont(font)
        self.label_Date2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Date2.setObjectName("label_Date2")
        self.horizontalLayout.addWidget(self.label_Date2)
        self.comboBox_DateEnd = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_DateEnd.setFont(font)
        self.comboBox_DateEnd.setObjectName("comboBox_DateEnd")
        self.horizontalLayout.addWidget(self.comboBox_DateEnd)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        #节次部分
        self.label_Section = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Section.setFont(font)
        self.label_Section.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Section.setObjectName("label_Section")
        self.horizontalLayout.addWidget(self.label_Section)
        self.comboBox_SectionStart = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_SectionStart.setFont(font)
        self.comboBox_SectionStart.setObjectName("comboBox_SectionStart")
        self.horizontalLayout.addWidget(self.comboBox_SectionStart)
        self.label_Section2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_Section2.sizePolicy().hasHeightForWidth())
        self.label_Section2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Section2.setFont(font)
        self.label_Section2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Section2.setObjectName("label_Section2")
        self.horizontalLayout.addWidget(self.label_Section2)
        self.comboBox_SectionEnd = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_SectionEnd.setFont(font)
        self.comboBox_SectionEnd.setObjectName("comboBox_SectionEnd")
        self.horizontalLayout.addWidget(self.comboBox_SectionEnd)
        #变量填充
        for i in range(len(week_items_list)):
            self.comboBox_WeekStart.addItem(week_items_list[i])
            self.comboBox_WeekEnd.addItem(week_items_list[i])
        self.comboBox_WeekStart.setCurrentIndex(self.WeekStart)
        self.comboBox_WeekEnd.setCurrentIndex(self.WeekEnd)
        for i in range(len(date_items_list)):
            self.comboBox_DateStart.addItem(date_items_list[i])
            self.comboBox_DateEnd.addItem(date_items_list[i])
        self.comboBox_DateStart.setCurrentIndex(self.DateStart)
        self.comboBox_DateEnd.setCurrentIndex(self.DateEnd)
        for i in range(len(section_items_list)):
            self.comboBox_SectionStart.addItem(section_items_list[i])
            self.comboBox_SectionEnd.addItem(section_items_list[i])
        self.comboBox_SectionStart.setCurrentIndex(self.SectionStart)
        self.comboBox_SectionEnd.setCurrentIndex(self.SectionEnd)
        #查询按钮
        self.pushButton_Search = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Search.sizePolicy().hasHeightForWidth())
        self.pushButton_Search.setSizePolicy(sizePolicy)
        self.pushButton_Search.clicked.connect(self.query)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_Search.setFont(font)
        self.pushButton_Search.setObjectName("pushButton_Search")
        self.horizontalLayout.addWidget(self.pushButton_Search)
        self.verticalLayout.addLayout(self.horizontalLayout)
        #第二行水平布局
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        #教室部分
        self.label_Classroom = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.label_Classroom.setFont(font)
        self.label_Classroom.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Classroom.setObjectName("label_Classroom")
        self.horizontalLayout_4.addWidget(self.label_Classroom)
        self.comboBox_Classroom = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_Classroom.setFont(font)
        self.comboBox_Classroom.setObjectName("comboBox_Classroom")
        self.comboBox_Classroom.setEditable(True)
        for i in range(len(classroom_items_list)):
            self.comboBox_Classroom.addItem(classroom_items_list[i])
        self.comboBox_Classroom.setCurrentIndex(-1)
        self.completer = QtWidgets.QCompleter(classroom_items_list)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_Classroom.setCompleter(self.completer)
        self.horizontalLayout_4.addWidget(self.comboBox_Classroom)
        self.label_Course = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        #课程名称部分
        self.label_Course.setFont(font)
        self.label_Course.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_Course.setObjectName("label_Course")
        self.horizontalLayout_4.addWidget(self.label_Course)
        self.comboBox_Course = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.comboBox_Course.setFont(font)
        self.comboBox_Course.setObjectName("comboBox_Course")
        self.comboBox_Course.setEditable(True)
        for i in range(len(course_items_list)):
            self.comboBox_Course.addItem(course_items_list[i])
        self.comboBox_Course.setCurrentIndex(-1)
        self.completer = QtWidgets.QCompleter(course_items_list)
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.completer.setCompletionMode(QtWidgets.QCompleter.PopupCompletion)
        self.comboBox_Course.setCompleter(self.completer)
        self.horizontalLayout_4.addWidget(self.comboBox_Course)
        self.checkBox_ShowOwn = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.checkBox_ShowOwn.setFont(font)
        self.checkBox_ShowOwn.setObjectName("checkBox_ShowOwn")
        self.horizontalLayout_4.addWidget(self.checkBox_ShowOwn)
        #返回按钮
        self.pushButton_Back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Back.sizePolicy().hasHeightForWidth())
        self.pushButton_Back.setSizePolicy(sizePolicy)
        self.pushButton_Back.clicked.connect(self.goBack)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_Back.setFont(font)
        self.pushButton_Back.setObjectName("pushButton_Back")
        self.horizontalLayout_4.addWidget(self.pushButton_Back)
        #重置按钮
        self.pushButton_Reset = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_Reset.sizePolicy().hasHeightForWidth())
        self.pushButton_Reset.setSizePolicy(sizePolicy)
        self.pushButton_Reset.clicked.connect(self.reset)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pushButton_Reset.setFont(font)
        self.pushButton_Reset.setObjectName("pushButton_Reset")
        self.horizontalLayout_4.addWidget(self.pushButton_Reset)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        
        #课表显示部分
        #初始化
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(1000, 450))
        self.tableWidget.setMaximumSize(QtCore.QSize(1280, 720))
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setRowCount(section_count)
        self.tableWidget.setColumnCount(date_count)
        self.tableWidget.setObjectName("tableWidget")
        #行列标题及表格格式初始化
        for i in range(len(section_items_list)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setVerticalHeaderItem(i, item)
            self.tableWidget.setRowHeight(i, 80)
        for i in range(len(date_items_list)):
            item = QtWidgets.QTableWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignCenter)
            font = QtGui.QFont()
            font.setFamily("微软雅黑")
            font.setPointSize(10)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(i, item)
            self.tableWidget.setColumnWidth(i, 150)
        for i in range(len(section_items_list)):
            for j in range(len(date_items_list)):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("微软雅黑 Light")
                font.setPointSize(10)
                item.setFont(font)
                item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                self.tableWidget.setItem(i, j, item)
        #表格自适应设置
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.gridLayout.addWidget(self.tableWidget, 4, 0, 1, 1)
        
        #进度条部分
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMinimumSize(QtCore.QSize(1000, 0))
        self.progressBar.setMaximumSize(QtCore.QSize(1280, 16777215))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 100)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 6, 0, 1, 1)
        self.progressBar.setVisible(False)
        MainWindow.setCentralWidget(self.centralwidget)
        
        #菜单栏部分
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 22))
        self.menubar.setObjectName("menubar")
        self.menu_Program = QtWidgets.QMenu(self.menubar)
        self.menu_Program.setObjectName("menu_Program")
        self.menu_Settings = QtWidgets.QMenu(self.menubar)
        self.menu_Settings.setObjectName("menu_Settings")
        self.menu_Help = QtWidgets.QMenu(self.menubar)
        self.menu_Help.setObjectName("menu_Help")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Import = QtWidgets.QAction(MainWindow)
        self.action_Import.setObjectName("action_Import")
        self.action_Exit = QtWidgets.QAction(MainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Background = QtWidgets.QAction(MainWindow)
        self.action_Background.setObjectName("action_Background")
        self.action_Spirit = QtWidgets.QAction(MainWindow)
        self.action_Spirit.setObjectName("action_Spirit")
        self.action_About = QtWidgets.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.menu_Program.addAction(self.action_Import)
        self.menu_Program.addSeparator()
        self.menu_Program.addAction(self.action_Exit)
        self.menu_Settings.addAction(self.action_Background)
        self.menu_Settings.addAction(self.action_Spirit)
        self.menu_Help.addAction(self.action_About)
        self.menubar.addAction(self.menu_Program.menuAction())
        self.menubar.addAction(self.menu_Settings.menuAction())
        self.menubar.addAction(self.menu_Help.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #绑定事件槽
        self.comboBox_WeekStart.activated.connect(self.combo_Week_active)
        self.comboBox_WeekEnd.activated.connect(self.combo_Week_active)
        self.comboBox_DateStart.activated.connect(self.combo_Date_active)
        self.comboBox_DateEnd.activated.connect(self.combo_Date_active)
        self.comboBox_SectionStart.activated.connect(self.combo_Section_active)
        self.comboBox_SectionEnd.activated.connect(self.combo_Section_active)
        self.comboBox_Classroom.activated.connect(self.combo_Classroom_active)
        self.comboBox_Course.activated.connect(self.combo_Course_active)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        
        #程序基本设定
        MainWindow.setWindowTitle(_translate("MainWindow", "2019211112班 2019-2020学年度第二学期课程表"))
        MainWindow.setWindowIcon(QtGui.QIcon("./icons/icon.ico"))
        qss = ""
        spirit_status = True
        try:
            setting = []
            with open('settings.ini', 'r', encoding='UTF-8') as f:
                for line in f:
                    setting.append(line)
            for i in range(len(setting)):
                t = setting[i].split('=',1)
                if t[0] == "background":
                    qss = "#MainWindow{border-image:url(" + t[1].strip() + ");}"
                    break
            else:
                qss = "#MainWindow{border-image:url(./bg.jpg);}"
            for i in range(len(setting)):
                t = setting[i].split('=',1)
                if t[0] == "spirit":
                    if "off" in t[1]:
                        spirit_status = False
                        break
                    else:
                        spirit_status = True
                        break
            else:
                spirit_status = True
        except:
            spirit_status = True
            qss = "#MainWindow{border-image:url(./bg.jpg);}"
        MainWindow.setStyleSheet(qss)
        if spirit_status:
            self.show_spirit()
        self.spirit_status = spirit_status
        
        #程序内部标签设定
        self.label_Title.setText(_translate("MainWindow", "2019211112班 2019-2020学年度第二学期课程表"))
        self.label_Week.setText(_translate("MainWindow", "周次"))
        self.label_Week2.setText(_translate("MainWindow", "至"))
        self.label_Date.setText(_translate("MainWindow", "日期"))
        self.label_Date2.setText(_translate("MainWindow", "至"))
        self.label_Section.setText(_translate("MainWindow", "节次"))
        self.label_Section2.setText(_translate("MainWindow", "至"))
        self.pushButton_Search.setText(_translate("MainWindow", "查询"))
        self.label_Classroom.setText(_translate("MainWindow", "教室"))
        self.label_Course.setText(_translate("MainWindow", "课程名称"))
        self.checkBox_ShowOwn.setText(_translate("MainWindow", "查询结果仅显示我的课程"))
        self.pushButton_Back.setText(_translate("MainWindow", "返回"))
        self.pushButton_Back.setVisible(False)
        self.pushButton_Reset.setText(_translate("MainWindow", "重置"))
        for i in range(len(section_items_list)):
            item = self.tableWidget.verticalHeaderItem(i)
            item.setText(_translate("MainWindow", section_items_timelist[i]))
        for i in range(len(date_items_list)):
            item = self.tableWidget.horizontalHeaderItem(i)
            item.setText(_translate("MainWindow", date_items_list[i]))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        for i in range(len(section_items_list)):
            for j in range(len(date_items_list)):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", classTable[i][j]))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.menu_Program.setTitle(_translate("MainWindow", "程序"))
        self.menu_Program.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menu_Settings.setTitle(_translate("MainWindow", "设置"))
        self.menu_Settings.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.menu_Help.setTitle(_translate("MainWindow", "帮助"))
        self.menu_Help.triggered[QtWidgets.QAction].connect(self.processtrigger)
        self.action_Import.setText(_translate("MainWindow", "导入课程表"))
        self.action_Exit.setText(_translate("MainWindow", "退出程序"))
        self.action_Background.setText(_translate("MainWindow", "更换界面背景"))
        if spirit_status:
            self.action_Spirit.setText(_translate("MainWindow", "关闭界面精灵"))
        else:
            self.action_Spirit.setText(_translate("MainWindow", "打开界面精灵"))
        self.action_About.setText(_translate("MainWindow", "关于"))

    def processtrigger(self,action):
        _translate = QtCore.QCoreApplication.translate
        if action.text() == "导入课程表":
            #课表导入过程
            try:
                openfile_name = QtWidgets.QFileDialog.getOpenFileName(self,'选择课表文件','','文本文档(*.txt)')
                if openfile_name[0] != '':
                    try:
                        getClassTable(openfile_name[0])
                        copyfile(openfile_name[0], 'curriculum.txt')
                        for i in range(len(section_items_list)):
                            for j in range(len(date_items_list)):
                                item = self.tableWidget.item(i, j)
                                item.setText(_translate("MainWindow", classTable[i][j]))
                        self.show_dialog('success')
                    except:
                        self.show_dialog('fail')
            except Exception as e:
                if str(e)!="[Errno 2] No such file or directory: ''":
                    self.show_dialog('fail')
        elif action.text() == "更换界面背景":
            #程序背景更换过程
            try:
                openfile_name = QtWidgets.QFileDialog.getOpenFileName(self,'选择背景图片','','所有图片文件(*.bmp;*.jpg;*.jpeg;*.jpe;*.png);;位图文件(*.bmp);;JPEG (*.jpg;*.jpeg;*.jpe);;PNG (*.png)')
                if openfile_name[0] != '':
                    try:
                        setting = []
                        with open('settings.ini', 'r', encoding='UTF-8') as f:
                            for line in f:
                                setting.append(line)
                        for i in range(len(setting)):
                            t = setting[i].split('=',1)
                            if t[0] == "background":
                                setting[i] = t[0] + "=" + openfile_name[0] + "\n"
                                break
                        else:
                            t = "background=" + openfile_name[0] + "\n"
                            setting.append(t)
                        with open('settings.ini', 'w', encoding='UTF-8') as f:
                            for i in range(len(setting)):
                                f.write(setting[i])
                        new_qss = "#MainWindow{border-image:url(" + openfile_name[0] + ");}"
                        self.MainWindow.setStyleSheet(new_qss)
                        self.show_dialog('success')
                    except:
                        self.show_dialog('fail')
            except Exception as e:
                if str(e)!="[Errno 2] No such file or directory: ''":
                    self.show_dialog('fail')
        elif action.text() == "关闭界面精灵":
            #界面精灵设置
            self.action_Spirit.setText(_translate("MainWindow", "打开界面精灵"))
            self.WidgetWindow.close()
            self.change_spirit_status("off")
            self.spirit_status = False
        elif action.text() == "打开界面精灵":
            #界面精灵设置
            self.action_Spirit.setText(_translate("MainWindow", "关闭界面精灵"))
            self.show_spirit()
            self.change_spirit_status("on")
            self.spirit_status = True
        elif action.text() == "关于":
            self.show_dialog('info')
        elif action.text() == "退出程序":
            self.exit_program()
            
    def show_dialog(self, status):
        #程序操作反馈对话框
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
        self.Dialog = QtWidgets.QDialog()
        ui = dialog.Ui_Dialog()
        ui.setupUi(self.Dialog, status)
        self.Dialog.show()
    
    def show_spirit(self):
        #显示界面精灵
        try:
            self.WidgetWindow.show()
        except:
            timestamp = time.localtime()
            time_status = 0
            for i in range(0,7):
                time_status = i
                if time_group[time_status] <= timestamp.tm_hour < time_group[time_status+1]:
                    break
            else:
                time_status = 7
            self.WidgetWindow = spirit.ShapeWidget(time_status)
            self.WidgetWindow.resize(250,250)
            self.WidgetWindow.show()
    
    def change_spirit_status(self, status):
        #更改界面精灵用户设置
        try:
            setting = []
            with open('settings.ini', 'r', encoding='UTF-8') as f:
                for line in f:
                    setting.append(line)
            for i in range(len(setting)):
                t = setting[i].split('=',1)
                if t[0] == "spirit":
                    setting[i] = t[0] + "=" + status + "\n"
                    break
            else:
                t = "spirit=" + status + "\n"
                setting.append(t)
            with open('settings.ini', 'w', encoding='UTF-8') as f:
                for i in range(len(setting)):
                    f.write(setting[i])
        except:
            a = 1

    def combo_Week_active(self, index):
        #绑定的周次改变事件
        
        if self.WeekStart != week_items_list.index(self.comboBox_WeekStart.currentText()):
            #开始周次
            self.WeekStart = week_items_list.index(self.comboBox_WeekStart.currentText())
            EndCount = self.comboBox_WeekEnd.count()
            for i in range(EndCount):
                self.comboBox_WeekEnd.removeItem(0)
            for i in range(20-self.WeekStart):
                self.comboBox_WeekEnd.addItem(week_items_list[self.WeekStart+i])
            if(self.WeekStart<self.WeekEnd):
                self.comboBox_WeekEnd.setCurrentIndex(self.WeekEnd-self.WeekStart)
            else:
                self.WeekEnd = self.WeekStart
        elif self.WeekEnd != week_items_list.index(self.comboBox_WeekEnd.currentText()):
            #结束周次
            self.WeekEnd = week_items_list.index(self.comboBox_WeekEnd.currentText())
            StartCount = self.comboBox_WeekStart.count()
            for i in range(StartCount):
                self.comboBox_WeekStart.removeItem(0)
            for i in range(self.WeekEnd+1):
                self.comboBox_WeekStart.addItem(week_items_list[i])
            if(self.WeekStart<self.WeekEnd):
                self.comboBox_WeekStart.setCurrentIndex(self.WeekStart)
            else:
                self.comboBox_WeekStart.setCurrentIndex(self.WeekEnd)
                self.WeekStart = self.WeekEnd

    def combo_Date_active(self, index):
        #绑定的星期改变事件
        
        if self.DateStart != date_items_list.index(self.comboBox_DateStart.currentText()):
            #开始星期
            self.DateStart = date_items_list.index(self.comboBox_DateStart.currentText())
            EndCount = self.comboBox_DateEnd.count()
            for i in range(EndCount):
                self.comboBox_DateEnd.removeItem(0)
            for i in range(5-self.DateStart):
                self.comboBox_DateEnd.addItem(date_items_list[self.DateStart+i])
            if(self.DateStart<self.DateEnd):
                self.comboBox_DateEnd.setCurrentIndex(self.DateEnd-self.DateStart)
            else:
                self.DateEnd = self.DateStart
        elif self.DateEnd != date_items_list.index(self.comboBox_DateEnd.currentText()):
            #结束星期
            self.DateEnd = date_items_list.index(self.comboBox_DateEnd.currentText())
            StartCount = self.comboBox_DateStart.count()
            for i in range(StartCount):
                self.comboBox_DateStart.removeItem(0)
            for i in range(self.DateEnd+1):
                self.comboBox_DateStart.addItem(date_items_list[i])
            if(self.DateStart<self.DateEnd):
                self.comboBox_DateStart.setCurrentIndex(self.DateStart)
            else:
                self.comboBox_DateStart.setCurrentIndex(self.DateEnd)
                self.DateStart = self.DateEnd

    def combo_Section_active(self, index):
        #绑定的节次改变事件
        
        if self.SectionStart != section_items_list.index(self.comboBox_SectionStart.currentText()):
            #开始节次
            self.SectionStart = section_items_list.index(self.comboBox_SectionStart.currentText())
            EndCount = self.comboBox_SectionEnd.count()
            for i in range(EndCount):
                self.comboBox_SectionEnd.removeItem(0)
            for i in range(14-self.SectionStart):
                self.comboBox_SectionEnd.addItem(section_items_list[self.SectionStart+i])
            if(self.SectionStart<self.SectionEnd):
                self.comboBox_SectionEnd.setCurrentIndex(self.SectionEnd-self.SectionStart)
            else:
                self.SectionEnd = self.SectionStart
        elif self.SectionEnd != section_items_list.index(self.comboBox_SectionEnd.currentText()):
            #结束节次
            self.SectionEnd = section_items_list.index(self.comboBox_SectionEnd.currentText())
            StartCount = self.comboBox_SectionStart.count()
            for i in range(StartCount):
                self.comboBox_SectionStart.removeItem(0)
            for i in range(self.SectionEnd+1):
                self.comboBox_SectionStart.addItem(section_items_list[i])
            if(self.SectionStart<self.SectionEnd):
                self.comboBox_SectionStart.setCurrentIndex(self.SectionStart)
            else:
                self.comboBox_SectionStart.setCurrentIndex(self.SectionEnd)
                self.SectionStart = self.SectionEnd
    
    def combo_Classroom_active(self, index):
        #绑定的教室改变事件
        self.Classroom = self.comboBox_Classroom.currentText()
    
    def combo_Course_active(self, index):
        #绑定的课程改变事件
        self.Course = self.comboBox_Course.currentText()
    
    def reset(self):
        #重置查询条件
        
        #重置数据
        self.WeekStart = 0
        self.WeekEnd = 15
        self.DateStart = 0
        self.DateEnd = 4
        self.SectionStart = 0
        self.SectionEnd = 13
        self.Classroom = ""
        self.Course= ""
        w_s_c = self.comboBox_WeekStart.count()
        w_e_c = self.comboBox_WeekEnd.count()
        d_s_c = self.comboBox_DateStart.count()
        d_e_c = self.comboBox_DateEnd.count()
        s_s_c = self.comboBox_SectionStart.count()
        s_e_c = self.comboBox_SectionEnd.count()
        #重置填充
        for i in range(w_s_c):
            self.comboBox_WeekStart.removeItem(0)
        for i in range(w_e_c):
            self.comboBox_WeekEnd.removeItem(0)
        for i in range(d_s_c):
            self.comboBox_DateStart.removeItem(0)
        for i in range(d_e_c):
            self.comboBox_DateEnd.removeItem(0)
        for i in range(s_s_c):
            self.comboBox_SectionStart.removeItem(0)
        for i in range(s_e_c):
            self.comboBox_SectionEnd.removeItem(0)
        for i in range(len(week_items_list)):
            self.comboBox_WeekStart.addItem(week_items_list[i])
            self.comboBox_WeekEnd.addItem(week_items_list[i])
        self.comboBox_WeekStart.setCurrentIndex(self.WeekStart)
        self.comboBox_WeekEnd.setCurrentIndex(self.WeekEnd)
        for i in range(len(date_items_list)):
            self.comboBox_DateStart.addItem(date_items_list[i])
            self.comboBox_DateEnd.addItem(date_items_list[i])
        self.comboBox_DateStart.setCurrentIndex(self.DateStart)
        self.comboBox_DateEnd.setCurrentIndex(self.DateEnd)
        for i in range(len(section_items_list)):
            self.comboBox_SectionStart.addItem(section_items_list[i])
            self.comboBox_SectionEnd.addItem(section_items_list[i])
        self.comboBox_SectionStart.setCurrentIndex(self.SectionStart)
        self.comboBox_SectionEnd.setCurrentIndex(self.SectionEnd)
        self.comboBox_Classroom.setCurrentIndex(-1)
        self.comboBox_Course.setCurrentIndex(-1)
    
    def goBack(self):
        #从查询结果返回上一层
        _translate = QtCore.QCoreApplication.translate
        for i in range(len(section_items_list)):
            for j in range(len(date_items_list)):
                item = self.tableWidget.item(i, j)
                item.setText(_translate("MainWindow", classTable[i][j]))
                self.tableWidget.item(i ,j).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
        try:
            sip.delete(self.tableWidget_result)
            self.tableWidget_result.setVisible(False)
            print('t')
        except:
            a = 1
        self.tableWidget.setVisible(True)
        self.pushButton_Back.setVisible(False)
    
    def query(self):
        #查询课程
        
        #周次判断
        def checkWeek(i,j):
            table = classTable[i][j].split()
            try:
                table[3] = table[3].replace("周","")
                flag = -1
                if "单" in table[3]:
                    flag = 1
                    table[3] = table[3].replace("单","")
                elif "双" in table[3]:
                    flag = 0
                    table[3] = table[3].replace("双","")
                week = table[3].split(",")
                for i2 in range(self.WeekStart+1,self.WeekEnd+2):
                    if flag >= 0:
                        if i2%2!=flag:
                            continue
                    for item in week:
                        t = item.split('-')
                        s = int(t[0])
                        e = 0
                        try:
                            e = int(t[1])
                        except:
                            e = s
                        if s <= i2 <= e:
                            return True
                            break
                else:
                    return False
            except:
                return False
        
        #拼接查询字符串
        def get_query_str(w_s,w_e,d_s,d_e,s_s,s_e,classroom,course):
            week_select_list=["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20"]
            week = "(week_s like '%" + week_select_list[w_s] + "%'"
            date = ") and (date like '%" + str(date_items_list[d_s]) + "%'"
            section = ") and (section like '%" + str(section_items_list[s_s]) + "%'"
            for i in range(w_s+1,w_e+1):
                week = week + " or week_s like '%" + week_select_list[i] + "%'"
            for i in range(d_s+1,d_e+1):
                date = date + " or date like '%" + str(date_items_list[i]) + "%'"
            for i in range(s_s+1,s_e+1):
                section = section + " or section like '%" + str(section_items_list[i]) + "%'"
            classroom_s = ") and classroom like '%" + classroom
            if(classroom!=""):
                classroom_s = classroom_s + "%"
            classroom_s = classroom_s + "'"
            course_s = " and course like '%" + course
            if(course!=""):
                course_s = course_s + "%"
            course_s = course_s + "'"
            t = week + date + section + classroom_s + course_s
            return t
        
        _translate = QtCore.QCoreApplication.translate
        self.progressBar.setProperty("value", 0)
        self.progressBar.setVisible(True)
        try:
            sip.delete(self.tableWidget_result)
        except:
            a = 1
        if self.checkBox_ShowOwn.isChecked():
            #查询自己的课程
            for i in range(len(section_items_list)):
                for j in range(len(date_items_list)):
                    item = self.tableWidget.item(i, j)
                    if checkWeek(i,j) and self.DateStart<=j<=self.DateEnd and self.SectionStart<=i<=self.SectionEnd and self.comboBox_Classroom.currentText() in classTable[i][j] and self.comboBox_Course.currentText() in classTable[i][j]:
                        item.setText(_translate("MainWindow", classTable[i][j]))
                        self.tableWidget.item(i ,j).setForeground(QtGui.QBrush(QtGui.QColor(255,0,0)))
                    else:
                        t = ''
                        item.setText(_translate("MainWindow", t))
                        self.tableWidget.item(i ,j).setForeground(QtGui.QBrush(QtGui.QColor(0,0,0)))
                    if(int((i*5+j+1)/70*100)>int((i*5+j)/70*100)):
                        self.progressBar.setProperty("value", int((i*5+j+1)/70*100))
            self.tableWidget.setVisible(True)
            try:
                self.tableWidget_result.setVisible(False)
            except:
                a = 1
        else:
            #查询全校课程
            
            #打开数据库
            conn = sqlite3.connect('timetable.db')
            c = conn.cursor()
            query_full_str = "select * from main where " + get_query_str(self.WeekStart,self.WeekEnd,self.DateStart,self.DateEnd,self.SectionStart,self.SectionEnd,self.comboBox_Classroom.currentText(),self.comboBox_Course.currentText())
            cursor = c.execute(query_full_str)
            #表格设置
            query_result = []
            for row in cursor:
                query_result.append(row)
            height = len(query_result)
            result_title = ['校区','教学楼','教室','周次','日期','节次','课程名称','授课教师','班级']
            result_width = [65,100,100,100,40,60,220,80,180]
            self.tableWidget_result = QtWidgets.QTableWidget(self.centralwidget)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tableWidget_result.sizePolicy().hasHeightForWidth())
            self.tableWidget_result.setSizePolicy(sizePolicy)
            self.tableWidget_result.setMinimumSize(QtCore.QSize(1000, 450))
            self.tableWidget_result.setMaximumSize(QtCore.QSize(1280, 720))
            self.tableWidget_result.setGridStyle(QtCore.Qt.SolidLine)
            self.tableWidget_result.setWordWrap(True)
            self.tableWidget_result.setRowCount(height)
            self.tableWidget_result.setColumnCount(9)
            self.tableWidget_result.setObjectName("tableWidget_result")
            self.gridLayout.addWidget(self.tableWidget_result, 5, 0, 1, 1)
            #表格填充
            for i in range(height):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                item.setFont(font)
                item.setText(str(i+1))
                self.tableWidget_result.setVerticalHeaderItem(i, item)
            for i in range(len(result_title)):
                item = QtWidgets.QTableWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                font = QtGui.QFont()
                font.setFamily("微软雅黑")
                font.setPointSize(10)
                item.setFont(font)
                item.setText(result_title[i])
                self.tableWidget_result.setHorizontalHeaderItem(i, item)
                self.tableWidget_result.setColumnWidth(i, result_width[i])
            for i in range(height):
                for j in range(0,3):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    font = QtGui.QFont()
                    font.setFamily("微软雅黑 Light")
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    item.setText(query_result[i][j])
                    self.tableWidget_result.setItem(i, j, item)
                for j in range(3,9):
                    item = QtWidgets.QTableWidgetItem()
                    item.setTextAlignment(QtCore.Qt.AlignCenter)
                    font = QtGui.QFont()
                    font.setFamily("微软雅黑 Light")
                    font.setPointSize(10)
                    item.setFont(font)
                    item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDragEnabled|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
                    item.setText(query_result[i][j+1])
                    self.tableWidget_result.setItem(i, j, item)
                if(int((i+1)/height*100)>int(i/height*100)):
                    self.progressBar.setProperty("value", int((i+1)/height*100))
            #表格自适应
            self.tableWidget_result.verticalHeader().setVisible(True)
            self.tableWidget_result.verticalHeader().setCascadingSectionResizes(False)
            self.tableWidget_result.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
            conn.close()
            self.tableWidget.setVisible(False)
        self.pushButton_Back.setVisible(True)
        self.progressBar.setVisible(False)
        
    def exit_program(self):
        #程序退出
        try:
            self.TrayWidget.hide()
        except:
            a = 1
        if self.spirit_status:
            try:
                self.WidgetWindow.close()
            except:
                a = 1
        try:
            self.MainWindow.close()
        except:
            a = 1