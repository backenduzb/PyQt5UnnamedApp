from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)
from utils.decorator import circularPixmap

from utils.style import readStyles


class ChatItem(QWidget):
    def __init__(self, avatar_path, full_name: str, last_message: str):
        super().__init__()

        avatar = QLabel()
        avatar.setObjectName("avatar")
        avatar.setFixedSize(QSize(70, 70))
        avatar.setPixmap(circularPixmap(avatar_path, 60))

        full_name_label = QLabel(full_name)
        full_name_label.setObjectName("full_name")
        last_message_label = QLabel(last_message)
        last_message_label.setObjectName("last_message")
        
        
        text_layout = QVBoxLayout()
        text_layout.addWidget(full_name_label)
        text_layout.addWidget(last_message_label)
        text_layout.setContentsMargins(8, 8, 8, 8)
        text_layout.setSpacing(1)

        main_layout = QHBoxLayout()
        main_layout.addWidget(avatar)
        main_layout.addLayout(text_layout)
        main_layout.setContentsMargins(5, 5, 5, 5)
        main_layout.setSpacing(0)
        
        self.setLayout(main_layout)
        self.setStyleSheet(readStyles("components/chatItem.css"))


class ChatMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.chatList = QListWidget()

        for i in range(2):
            chat = QListWidgetItem()
            widget = ChatItem("assets/profile.jpg", "Michael Kaiser", "こんいちわ！　どぞ　よろしく")
            chat.setSizeHint(widget.sizeHint())
            self.chatList.addItem(chat)
            self.chatList.setItemWidget(chat, widget)
            
        layout = QVBoxLayout()
        layout.addWidget(self.chatList)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatMenu.css"))
        self.setContentsMargins(0, 0, 0, 0)
        