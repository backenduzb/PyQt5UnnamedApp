from PyQt5.QtWidgets import QScrollArea


class SmoothScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.verticalScrollBar().setSingleStep(1)
        self.verticalScrollBar().setPageStep(1)

    def wheelEvent(self, event):

        pixel_delta = event.pixelDelta().y()

        if pixel_delta == 0:
            pixel_delta = event.angleDelta().y() / 120

        scroll_value = self.verticalScrollBar().value() - pixel_delta

        self.verticalScrollBar().setValue(int(scroll_value))