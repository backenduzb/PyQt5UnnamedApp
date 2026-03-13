from PyQt5.QtWidgets import (
    QVBoxLayout, QWidget, QLabel, QHBoxLayout
)
from utils.style import readStyles

class TitlePanel(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QHBoxLayout()
        name_layout = QVBoxLayout()
        
        self.full_name_panel = QLabel("Michael Kaiser")
        self.last_seen = QLabel("last seen recently")
        layout.addLayout(layout, )
        
        self.setStyleSheet(readStyles("components/chatarea/titlePanel.css"))