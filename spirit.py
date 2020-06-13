import sys, time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QCursor, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip, QMenu, QAction
import PyQt5.QtCore as QtCore


class ShapeWidget(QWidget):
    def __init__(self, time_status, parent_addr=None, parent=None):
        super(ShapeWidget, self).__init__(None)
        desktop = QApplication.desktop()

        self.parent_addr = parent_addr
        self.parent = parent
        self.time_status = time_status
        self.mypix()
        self.setWindowTitle("学习精灵")
        self.setWindowIcon(QIcon('./icons/icon.ico'))
        self.move(desktop.width() * 0.85, desktop.height() * 0.68)

        self.menu = QMenu()
        self.showAction = QAction("显示/隐藏窗口",
                                  self,
                                  triggered=self.change_windows)
        self.quitAction = QAction("退出", self, triggered=self.quitProgram)
        self.menu.addAction(self.showAction)
        self.menu.addAction(self.quitAction)

    # 图片蒙版
    def mypix(self):
        bitmap_pos = './spirit/spirit0' + str(self.time_status) + '.jpg'
        self.pix = QBitmap(bitmap_pos)
        self.dragPosition = None
        self.setMask(self.pix)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 设置置顶窗口样式

    # 使不规则窗体能响应鼠标事件，随意拖动。
    def mousePressEvent(self, event):
        if event.type() == QtCore.QEvent.MouseButtonDblClick:
            if self.parent.isVisible():
                self.parent.hide()
            else:
                self.parent.show()
                self.parent.raise_()
        elif event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        if event.button() == Qt.RightButton:
            self.menu.exec_(QCursor.pos())

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_drag:
            # 当左键移动窗体修改偏移值
            self.move(QMouseEvent.globalPos() - self.m_DragPosition)
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def paintEvent(self, event):
        painter = QPainter(self)
        pixmap_pos = './spirit/spirit0' + str(self.time_status) + '.png'
        painter.drawPixmap(0, 0, self.width(), self.height(),
                           QPixmap(pixmap_pos))

    def change_windows(self):
        if self.parent.isVisible():
            self.parent.hide()
        else:
            self.parent.show()
            self.parent.raise_()

    def quitProgram(self):
        self.setVisible(False)
        self.parent_addr.exit_program()
