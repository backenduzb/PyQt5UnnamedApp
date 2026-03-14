from PyQt5.QtWidgets import QWidget, QLabel, QListWidget
from utils.style import readStyles

class ChatArea(QWidget):
    def __init__(self):
        super().__init__()
        
        chatList = QListWidget()
        
        self.setStyleSheet(readStyles("components/chatarea/chatArea.css"))