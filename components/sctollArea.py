from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QPushButton, QScrollArea, QVBoxLayout, QWidget


class SmoothScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QScrollArea.NoFrame)

        self.ani = QPropertyAnimation(self.verticalScrollBar(), b"value")
        self.ani.setEasingCurve(QEasingCurve.OutQuart)
        self.ani.setDuration(600)

        self.target_value = 0

    def wheelEvent(self, event):
        delta = event.angleDelta().y()

        step = delta * 2

        if self.ani.state() == QPropertyAnimation.Running:
            new_target = self.target_value - step
        else:
            new_target = self.verticalScrollBar().value() - step

        self.target_value = max(
            self.verticalScrollBar().minimum(),
            min(new_target, self.verticalScrollBar().maximum()),
        )

        self.ani.stop()
        self.ani.setStartValue(self.verticalScrollBar().value())
        self.ani.setEndValue(self.target_value)
        self.ani.start()
