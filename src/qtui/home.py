import datetime
import webbrowser

from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap, QCursor
from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QSpacerItem, QSizePolicy


class ClickableLabel(QLabel):
    clicked = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit()
        super().mousePressEvent(event)


class ClickableLinkLabel(QLabel):
    def __init__(self, text, url, parent=None):
        super().__init__(parent)
        self.text_content = text
        self.url = url
        self.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.update_style(hover=False)

    def update_style(self, hover=False):
        color = "#ff4444" if hover else "#cc3333"
        style = f"color: {color}; font-size: 14px; font-weight: bold; background: transparent; border: none;"
        if "yours" in self.text_content:
            style += " text-decoration: underline;"
        self.setStyleSheet(style)
        self.setText(self.text_content)

    def enterEvent(self, event):
        self.update_style(hover=True)
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.update_style(hover=False)
        super().leaveEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            webbrowser.open(self.url)
        super().mousePressEvent(event)


class HomePage(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("HomePage")

        self.react_click_count = 0
        self._last_react_time = None

        self.raw_pixmap = QPixmap("bin/kemiaojiang.png")

        self.initUI()

    def initUI(self):
        main_layout = QHBoxLayout(self)
        main_layout.setContentsMargins(80, 60, 80, 60)
        main_layout.setSpacing(0)

        left_container = QWidget(self)
        left_container.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)

        self.left_layout = QVBoxLayout(left_container)
        self.left_layout.setContentsMargins(0, 0, 0, 0)

        self.avatar_label = ClickableLabel()
        self.avatar_label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.avatar_label.clicked.connect(self.react)

        self.left_layout.addWidget(self.avatar_label)
        self.left_layout.addStretch()

        mid_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Minimum)

        right_container = QWidget(self)
        right_container.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)

        right_layout = QVBoxLayout(right_container)
        right_layout.setSpacing(90)
        right_layout.setContentsMargins(0, 20, 0, 0)

        info_text = (
            "<span style='color: #4ba3e3; font-weight: bold; font-size: 17px; font-family: Consolas, Microsoft YaHei;'>Ambassador:</span> "
            "<span style='color: #ffffff; font-size: 17px; font-family: Consolas;'>KeMiaoJiang</span><br>"
            "<span style='color: #4ba3e3; font-weight: bold; font-size: 17px; font-family: Consolas, Microsoft YaHei;'>Painter:</span> "
            "<span style='color: #ffffff; font-size: 17px; font-family: Microsoft YaHei;'>HY-惠</span><br>"
            "<span style='color: #4ba3e3; font-weight: bold; font-size: 17px; font-family: Consolas;'>Welcome To MIO-KITCHEN</span>"
        )
        info_label = QLabel(info_text)
        info_label.setStyleSheet("line-height: 160%; background: transparent;")
        right_layout.addWidget(info_label)

        campaign_card = QWidget(self)
        campaign_card.setStyleSheet(
            "QWidget { background-color: #121212; border-radius: 8px; border: 1px solid #232323; }")
        campaign_card.setMinimumWidth(360)
        campaign_card.setMaximumWidth(550)

        card_layout = QVBoxLayout(campaign_card)
        card_layout.setSpacing(16)
        card_layout.setContentsMargins(28, 24, 28, 28)

        card_title = QLabel("Campaign & Community", campaign_card)
        card_title.setStyleSheet(
            "color: #757575; font-size: 13px; font-weight: 500; border: none; background: transparent;")

        sub_text_1 = ClickableLinkLabel("Your phone is about to stop being yours.", "http://127.0.0.1", campaign_card)
        sub_text_2 = ClickableLinkLabel("Keep Android Open", "http://127.0.0.1", campaign_card)

        card_layout.addWidget(card_title)
        card_layout.addWidget(sub_text_1)
        card_layout.addWidget(sub_text_2)

        right_layout.addWidget(campaign_card)
        right_layout.addStretch()

        right_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        main_layout.addWidget(left_container, stretch=4)
        main_layout.addItem(mid_spacer)
        main_layout.addWidget(right_container, stretch=6)
        main_layout.addItem(right_spacer)

        self.setStyleSheet("background-color: transparent;")

    def resizeEvent(self, event):
        super().resizeEvent(event)
        available_width = max(100, self.avatar_label.width())
        available_height = max(100, self.avatar_label.height())

        scaled_pixmap = self.raw_pixmap.scaled(
            available_width,
            available_height,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation
        )
        self.avatar_label.setPixmap(scaled_pixmap)

    def react(self):
        current_time = datetime.datetime.now()
        if self._last_react_time and (current_time - self._last_react_time).total_seconds() < 0.6:
            return
        self._last_react_time = current_time
        self.react_click_count += 1

        print(f"count: {self.react_click_count}")
        if self.react_click_count >= 15:
            self.react_click_count = 0
