from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt
from utils.style import readStyles


class HomeScreen(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        label = QLabel("Welcome")
        layout.addWidget(label)
        
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        
        self.setLayout(layout)
        self.setStyleSheet(readStyles("screens/homeScreen.css"))