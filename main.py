import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from utils.style import readStyles


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("QAPP")
        self.setStyleSheet(readStyles("mainWindow.css"))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
