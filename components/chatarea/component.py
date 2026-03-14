from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QWidget

from utils.style import readStyles

from .sendpanel import SendPanel
from .titlepanel import TitlePanel
from .area import ChatArea

class ChatComponent(QWidget):
    def __init__(self):
        super().__init__()

        title_panel = TitlePanel()
        send_panel = SendPanel()
        chat_area = ChatArea()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(title_panel)
        layout.addWidget(chat_area)
        layout.addWidget(send_panel)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.setObjectName("main")
        self.setStyleSheet(readStyles("components/chatarea/chatComponent.css"))