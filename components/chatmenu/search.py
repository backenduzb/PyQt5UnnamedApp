from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QLineEdit,
    QVBoxLayout,
    QWidget,
)

from utils.style import readStyles


class SearchHeader(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(40, 20, 8, 8)

        self.search = QLineEdit()
        self.search.setFixedHeight(40)
        self.search.setPlaceholderText("Search")

        layout.addWidget(self.search)
        self.setMaximumWidth(455)
        self.setLayout(layout)

        self.setObjectName("main")
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setStyleSheet(readStyles("components/chatmenu/searchHeader.css"))
