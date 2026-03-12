from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QFrame, QLabel, QScrollArea,
    QSizePolicy, QVBoxLayout,
    QWidget,
)

from components.chatMenu import ChatMenu
from utils.style import readStyles


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        label = QLabel("Welcome")
        label.setAlignment(Qt.AlignmentFlag.AlignRight)
        font = label.font()
        font.setPointSize(14)
        label.setFont(font)
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignRight)

        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.Shape.NoFrame)
        
        chat_menu = ChatMenu()
        scroll.setWidget(chat_menu)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding)
        
        layout.setContentsMargins(0, 0, 0, 0) 
        layout.addWidget(scroll, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)
        self.setStyleSheet(readStyles("screens/homeScreen.css"))
