from PyQt5.QtWidgets import QSizePolicy, QVBoxLayout, QWidget

from .sendpanel import SendPanel
from .titlepanel import TitlePanel


class ChatArea(QWidget):
    def __init__(self):
        super().__init__()

        title_panel = TitlePanel()
        send_panel = SendPanel()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        layout.addWidget(title_panel)
        layout.addStretch()
        layout.addWidget(send_panel)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
