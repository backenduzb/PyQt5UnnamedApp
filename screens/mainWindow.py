from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QScrollArea,
    QVBoxLayout,
    QWidget,
)

from components.chatMenu import (
    ChatMenu, SearchHeader
)
from utils.style import readStyles


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        search_header = SearchHeader()
        layout.addWidget(search_header, alignment=Qt.AlignmentFlag.AlignTop)
    
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setMinimumWidth(455)
        scroll.setMinimumHeight(600)
        scroll.setWidgetResizable(True)
        scroll.setLineWidth(0)
        scroll.setContentsMargins(0, 0, 0, 0)
        scroll.viewport().setContentsMargins(0, 0, 0, 0)
        
        chat_menu = ChatMenu()
        scroll.setWidget(chat_menu)
        chat_menu.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(scroll, alignment=Qt.AlignmentFlag.AlignLeft)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.setStyleSheet(readStyles("screens/homeScreen.css"))
