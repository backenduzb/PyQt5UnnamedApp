from PyQt5.QtCore import QEvent, Qt, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QVBoxLayout,
    QWidget,
)

from controllers.components.chatMenu import filterChats, handle_alt_navigation
from utils.style import readStyles

from PyQt5.QtWidgets import QGraphicsOpacityEffect

from .chatitem import ChatItem
from .search import SearchHeader


class ChatMenu(QWidget):
    def __init__(self):
        super().__init__()

        self.chatList = QListWidget()
        self.chatList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatList.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatList.verticalScrollBar().setSingleStep(8)
        
        self.chatList.setObjectName("chatList")
        self.scrollbar = self.chatList.verticalScrollBar()
        
        self.opacity = QGraphicsOpacityEffect()
        self.scrollbar.setGraphicsEffect(self.opacity)
        
        self.anim = QPropertyAnimation(self.opacity, b"opacity")
        self.anim.setDuration(200)
        self.anim.setEasingCurve(QEasingCurve.OutCubic)
        
        self.opacity.setOpacity(0)  

        self.searchHeader = SearchHeader()

        self.noChatsLabel = QLabel("No chats found")
        self.noChatsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
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
        layout.addWidget(self.noChatsLabel)
        layout.setContentsMargins(0, 0, 0, 0)

        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatmenu/chatMenu.css"))
        self.chatList.installEventFilter(self)

        self.searchHeader.search.textChanged.connect(
            lambda text: filterChats(self, text)
        )

    def eventFilter(self, source, event):
        if source is self.chatList:
            if event.type() == QEvent.Enter:
                self.showScrollbar()
            elif event.type() == QEvent.Leave:
                self.hideScrollbar()
            elif event.type() == QEvent.KeyPress:
                if handle_alt_navigation(self, event):
                    return True

        return super().eventFilter(source, event)

    def showScrollbar(self):
        self.scrollbar.show()
        self.anim.stop()
        self.anim.setStartValue(self.opacity.opacity())
        self.anim.setEndValue(1)
        self.anim.start()
    
    
    def hideScrollbar(self):
        self.anim.stop()
        self.anim.setStartValue(self.opacity.opacity())
        self.anim.setEndValue(0)
        self.anim.start()