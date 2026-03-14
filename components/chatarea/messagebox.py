from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
from utils.style import readStyles

class MessageBox(QWidget):
    def __init__(self, message):
        super().__init__()
        
        layout = QHBoxLayout()
        message = QLabel(message)
        
        
        layout.addWidget(message)
        self.setMinimumHeight(10)
        self.setMinimumWidth(80)
        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatarea/messageBox.css"))