from PyQt5.QtWidgets import QListWidgetItem, QWidget, QListWidget, QVBoxLayout
from PyQt5.QtCore import QSize, Qt
from utils.style import readStyles

class ChatMenu(QWidget):
    def __init__(self):
        super().__init__()
        
        self.chatList = QListWidget()

        for i in range(10):
            chat = QListWidgetItem(f"Chat {i}")
            chat.setSizeHint(QSize(300, 50)) 
            self.chatList.addItem(chat)
        
        layout = QVBoxLayout()
        layout.addWidget(self.chatList)
        self.setLayout(layout)

        self.setStyleSheet(readStyles("components/chatMenu.css"))