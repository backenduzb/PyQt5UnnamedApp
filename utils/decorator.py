from PyQt5.QtGui import QPixmap, QPainter, QBrush, QPen
from PyQt5.QtCore import Qt


def circularPixmap(path, size):
    pixmap = QPixmap(path).scaled(size, size, Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
    
    result = QPixmap(size, size)
    result.fill(Qt.GlobalColor.transparent)

    painter = QPainter(result)
    painter.setRenderHint(QPainter.Antialiasing) 
    painter.setRenderHint(QPainter.SmoothPixmapTransform)

    brush = QBrush(pixmap)
    painter.setBrush(brush)
    painter.setPen(Qt.PenStyle.NoPen)
    painter.drawEllipse(0, 0, size, size)

    painter.end()
    return result
