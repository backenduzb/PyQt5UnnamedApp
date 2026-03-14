from PyQt5.QtWidgets import QHBoxLayout, QSizePolicy, QWidget

from components.chatarea import ChatComponent
from components.chatmenu import ChatMenu
from utils.style import readStyles


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        chat_menu = ChatMenu()
        chat_menu.setFixedWidth(455)
        chat_menu.setMinimumHeight(600)

        chat_area = ChatComponent()
        chat_area.setMinimumHeight(600)
        chat_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        layout.addWidget(chat_menu)
        layout.addWidget(chat_area, 1)

        self.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        self.setStyleSheet(readStyles("screens/homeScreen.css"))
