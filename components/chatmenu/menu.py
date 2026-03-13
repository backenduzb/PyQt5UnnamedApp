from PyQt5.QtCore import QEvent, QSize, Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QScrollArea,
    QWidget,
)

from controllers.components.chatMenu import filterChats, handle_alt_navigation
from utils.style import readStyles

from .chatitem import ChatItem
from .search import SearchHeader


class ChatMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.chatList = QListWidget()
        self.chatList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatList.verticalScrollBar().setSingleStep(8)
        self.searchHeader = SearchHeader()

        self.noChatsLabel = QLabel("No chats found")
        self.noChatsLabel.setAlignment(Qt.AlignmentFlag.AlignVCenter)
        self.noChatsLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.noChatsLabel.hide()

        for i in range(200):
            chat = QListWidgetItem()
            widget = ChatItem(
                "assets/profile.jpg",
                "Michael Kaiser",
                f"こんいちわ！　どぞ　よろしく {i}",
            )
            chat.setSizeHint(widget.sizeHint())
            self.chatList.addItem(chat)
            self.chatList.setItemWidget(chat, widget)

        layout = QVBoxLayout()
        layout.addWidget(self.searchHeader)
        layout.addWidget(self.chatList)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.noChatsLabel)

        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatMenu.css"))
        self.setContentsMargins(0, 0, 0, 0)
        self.chatList.installEventFilter(self)
        self.searchHeader.search.textChanged.connect(
            lambda text: filterChats(self, text)
        )

    def eventFilter(self, source, event):
        if source is self.chatList and event.type() == QEvent.Type.KeyPress:
            if handle_alt_navigation(self, event):
                return True

        return super().eventFilter(source, event)
