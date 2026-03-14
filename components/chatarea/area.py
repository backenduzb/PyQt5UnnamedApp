from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QListWidgetItem
from utils.style import readStyles

class ChatArea(QWidget):
    def __init__(self):
        super().__init__()
        
        self.chatList = QListWidget()
        self.chatList.setObjectName("chatArea")
        self.chatList.setContentsMargins(0, 0, 0, 0)
        
        for i in range(20):
            item = QListWidgetItem("Salom")
            self.chatList.addItem(item)
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.chatList)
        
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(readStyles("components/chatarea/chatArea.css"))