from PyQt5.QtWidgets import QWidget, QHBoxLayout, QListWidget, QListWidgetItem, QAbstractItemView
from utils.style import readStyles
from .messagebox import MessageBox

class ChatArea(QWidget):
    def __init__(self):
        super().__init__()
        
        self.chatList = QListWidget()
        self.chatList.setObjectName("chatArea")
        self.chatList.setContentsMargins(0, 0, 0, 0)
        self.chatList.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.chatList.verticalScrollBar().setSingleStep(8)
        # self.chatList.setEnabled(False)
        # self.chatList.setSelectionMode(QAbstractItemView.NoSelection)
        
        for i in range(10):
            item = QListWidgetItem()
            message_box = MessageBox(f"Test uchun bu habarni jonatdim {i}", this_me=True)
            
            item.setSizeHint(message_box.sizeHint())
            self.chatList.addItem(item)
            self.chatList.setItemWidget(item, message_box)
        
        for i in range(10):
            item = QListWidgetItem()
            message_box = MessageBox(f"Men ham buin test uchun jonatdim menimcha hozircha yaxshi ishlayapti {i}, ajoyib hozircha message boxlar tog;ri ishlayapti endi kattaroq matnlar bilan test qilish kerak", this_me=False)
            
            item.setSizeHint(message_box.sizeHint())
            self.chatList.addItem(item)
            self.chatList.setItemWidget(item, message_box)
        
        
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.chatList)
        
        self.setLayout(layout)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(readStyles("components/chatarea/chatArea.css"))