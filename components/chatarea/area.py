from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget
)

class ChatArea(QWidget):
    def __init__(self):
        super().__init__()
        
        self.layout = QVBoxLayout()
        