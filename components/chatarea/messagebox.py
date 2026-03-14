from PyQt5.QtWidgets import QLabel, QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from utils.style import readStyles

class MessageBox(QWidget):
    def __init__(self, message: str, this_me: bool):
        super().__init__()
        
        layout = QHBoxLayout()
        
        message_label = QLabel(message)
        message_label.setObjectName("message-text" if this_me else "message-text-other")
        
        message_label.setWordWrap(True)
        message_label.setMaximumWidth(800)
        
        if this_me:
            layout.setAlignment(Qt.AlignRight)
            layout.setContentsMargins(1, 1, 1, 1)
        else:
            layout.setAlignment(Qt.AlignLeft)
            layout.setContentsMargins(1, 1, 1, 1)
        
        layout.addWidget(message_label)
        
        self.setLayout(layout)
        self.setStyleSheet(readStyles("components/chatarea/messageBox.css"))
        self.setSizePolicy(message_label.sizePolicy())
        self.setMinimumHeight(30)