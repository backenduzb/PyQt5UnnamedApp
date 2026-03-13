from PyQt5.QtCore import QEvent, QSize, Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from controllers.components.chatMenu import filterChats, handle_alt_navigation
from utils.decorator import circularPixmap
from utils.style import readStyles


class SearchHeader(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 20, 8, 8)

        self.search = QLineEdit()
        self.search.setFixedHeight(40)
        self.search.setPlaceholderText("Search")

        layout.addWidget(self.search)
        self.setMaximumWidth(455)
        self.setLayout(layout)

        self.setObjectName("main")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(readStyles("components/searchHeader.css"))


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
        main_layout.setContentsMargins(10, 5, 5, 5)
        main_layout.setSpacing(0)

        self.setLayout(main_layout)
        self.setStyleSheet(readStyles("components/chatItem.css"))


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
