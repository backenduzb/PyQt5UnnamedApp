from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel


def filterChats(self, text):
    text = text.lower()
    visible_count = 0

    for i in range(self.chatList.count()):
        item = self.chatList.item(i)
        widget = self.chatList.itemWidget(item)

        name = widget.findChild(QLabel, "full_name").text().lower()
        message = widget.findChild(QLabel, "last_message").text().lower()

        if text in name or text in message:
            item.setHidden(False)
            visible_count += 1
        else:
            item.setHidden(True)

    self.noChatsLabel.setVisible(visible_count == 0)


def handle_alt_navigation(chat_menu, event):
    if event.modifiers() & Qt.KeyboardModifier.AltModifier and event.key() in (Qt.Key.Key_Up, Qt.Key.Key_Down):
        count = chat_menu.chatList.count()
        if count == 0:
            return False

        current_row = chat_menu.chatList.currentRow()
        if current_row < 0:
            current_row = 0

        if event.key() == Qt.Key.Key_Up:
            target = max(0, current_row - 1)
        else:
            target = min(count - 1, current_row + 1)

        if target != current_row:
            chat_menu.chatList.setCurrentRow(target)
        return True

    return False
