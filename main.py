import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import Qt
from threading import Timer

import windows
from data import *


def show_toast(title, desc):
    ui.TrayWidget.show_toast(title, desc)


if __name__ == '__main__':
    #获取当前时间（日期及详细时间）
    timestamp = time.localtime(int(time.time() + 300))
    current_date = timestamp.tm_wday
    current_time = timestamp.tm_hour * 3600 + timestamp.tm_min * 60 + timestamp.tm_sec

    #开启高分屏适配
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)

    #从curriculum.txt获取用户课表，并计算当天要提醒的课程
    getClassTable()
    today_classes = []
    today_times = []
    if current_date < 5:
        for i in range(14):
            if classTable[i][current_date] != "" and current_time < timeTable[
                    i] and (len(today_classes) == 0 or
                            today_classes[-1] != classTable[i][current_date]):
                today_classes.append(classTable[i][current_date])
                today_times.append(timeTable[i] - current_time)
    for i in range(len(today_classes)):
        try:
            t = today_classes[i].split()
            today_classes[i] = t[0] + " " + t[2] + " " + t[3] + " " + t[1]
        except:
            today_classes[i] = today_classes[i].replace("\n", " ")

    #创建窗口应用实例
    MainWindow = QMainWindow()
    ui = windows.Ui_MainWindow()
    ui.setupUi(MainWindow)

    #设置定时器
    timers = []
    for i in range(len(today_classes)):
        timers.append(
            Timer(today_times[i], show_toast,
                  ("提醒上课小助手 - 距上课还有5分钟", today_classes[i])))
        timers[i].start()

    MainWindow.show()

    sys.exit(app.exec_())
