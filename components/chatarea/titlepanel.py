from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QLabel, QHBoxLayout
)
from utils.style import readStyles

class NameWidget(QWidget):
    def __init__(self, full_name: str, last_seen: str):
        super().__init__()
        
        layout = QVBoxLayout()
        
        full_name = QLabel(full_name)
        full_name.setObjectName("full_name")
        last_seen = QLabel(last_seen)
        last_seen.setObjectName("last_seen")
        
        layout.addWidget(full_name, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addWidget(last_seen, alignment=Qt.AlignmentFlag.AlignBottom)
        
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        
class TitlePanel(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        name = NameWidget("Michael Kaiser", "last seen recently")
        
        layout.addWidget(name, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatarea/titlePanel.css"))