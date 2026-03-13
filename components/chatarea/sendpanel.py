from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QHBoxLayout, QLineEdit, QSizePolicy, QWidget

from utils.style import readStyles


class SendPanel(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()

        message = QLineEdit()
        message.setPlaceholderText("Write a message ...")

        message.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        message.setMinimumWidth(0)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(message, 1)

        self.setLayout(layout)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setStyleSheet(readStyles("components/chatarea/titlePanel.css"))
