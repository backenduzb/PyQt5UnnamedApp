import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from screens.home import HomeScreen
from PyQt5.QtCore import QSize

from utils.style import readStyles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QAPP")
        
        self.pages = QStackedWidget()
        self.home = HomeScreen()
        
        self.pages.addWidget(self.home)
        self.setCentralWidget(self.pages)
        
        self.setStyleSheet(readStyles("mainWindow.css"))
        self.setFixedSize(QSize(600, 600))

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
