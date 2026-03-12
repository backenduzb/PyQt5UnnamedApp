import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from screens.mainWindow import HomeScreen

from utils.style import readStyles

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.pages = QStackedWidget()
        self.home = HomeScreen()
        
        self.pages.addWidget(self.home)
        self.setCentralWidget(self.pages)
        
        self.setStyleSheet(readStyles("mainWindow.css"))

app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec()
