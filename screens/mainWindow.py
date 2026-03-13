from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout, QWidget

from components.chatmenu import ChatMenu
from utils.style import readStyles


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        chat_menu = ChatMenu()
        chat_menu.setMinimumWidth(455)
        layout.addWidget(chat_menu, alignment=Qt.AlignmentFlag.AlignLeft)
        
        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

        self.setStyleSheet(readStyles("screens/homeScreen.css"))
