import sys,time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QCursor, QIcon
from PyQt5.QtWidgets import QWidget, QApplication, QToolTip
import PyQt5.QtCore as QtCore

class ShapeWidget(QWidget):
    def __init__(self, time_status, parent=None):
        super(ShapeWidget, self).__init__(parent)
        desktop = QApplication.desktop()

        self.time_status = time_status
        self.mypix()
        self.setWindowTitle("学习精灵")
        self.setWindowIcon(QIcon('./icons/icon.ico'))
        self.move(desktop.width()*0.85,desktop.height()*0.68)

    # 图片蒙版
    def mypix(self):
        bitmap_pos = './spirit/spirit0' + str(self.time_status) + '.jpg'
        self.pix = QBitmap(bitmap_pos)
        self.dragPosition = None
        self.setMask(self.pix)
        self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)  # 设置置顶窗口样式

    # 使不规则窗体能响应鼠标事件，随意拖动。
    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = event.globalPos() - self.pos()
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
        if event.button() == Qt.RightButton:
            self.close()

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
        painter.drawPixmap(0, 0, self.width(), self.height(), QPixmap(pixmap_pos))
