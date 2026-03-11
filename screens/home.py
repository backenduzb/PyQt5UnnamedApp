from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from utils.style import readStyles

class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()
        
        layout = QVBoxLayout()
        
        label = QLabel("Undefined name")
        layout.addWidget(label)
        
        self.setLayout(layout)
        self.setStyleSheet(readStyles("screens/homeScreen.css"))