import random

from math import sqrt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QBoxLayout, QMessageBox, QLabel

from . import DIFFICULTIES, WINDOW_HIGHT
from .widgets import MyColor


class MyChooserLayout(QGridLayout):
    def __init__(self, parent: "ChooserPage", *args, **kwargs):
        """Initialize the Label with a bigger Font Size"""
        super().__init__(*args, **kwargs)
        self.parent: "ChooserPage" = parent

        self.colors: list[MyColor] = []

    def setup_colors(self, difficulty):
        self.colors.clear()
        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)

        print(difficulty)
        per = int(sqrt(DIFFICULTIES.get(difficulty)))
        print(per)
        for i in range(DIFFICULTIES.get(difficulty)):
            self.colors.append(MyColor(self.generate_color(), (int(WINDOW_HIGHT/per), int(WINDOW_HIGHT/per)), self))
            self.addWidget(self.colors[-1], i // per, i % per)

    def generate_color(self):
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        while color in [col.rgb for col in self.colors]:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color


class MyGameLayout(QBoxLayout):
    def __init__(self, parent: "ChooserPage"):
        super().__init__(QBoxLayout.Direction.TopToBottom, parent)

        self.color = None
        self.parent = parent
        self.target = QLabel("Target Color")
        self.target.setStyleSheet(f"font-size: 30px")
        self.target.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tries = QLabel(f"Tries: {self.parent.tries}")
        self.tries.setStyleSheet("font-size: 20px")
        self.tries.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.addWidget(self.target)
        self.addWidget(self.tries)

    def set_new_color(self):
        self.parent.chooser.setup_colors(self.parent.difficulty)
        self.color = random.choice([col.rgb for col in self.parent.chooser.colors])
        self.target.setStyleSheet(f"background-color: rgb{self.color}")
        self.tries.setText(f"Tries: {self.parent.tries}")

    def update_tries(self, color: tuple[int, int, int]):
        if color != self.color:
            self.parent.tries += 1
            self.tries.setText(f"Tries: {self.parent.tries}")
            return False
        else:
            self.parent.tries += 1
            self.tries.setText(f"Tries: {self.parent.tries}")
            QMessageBox.information(self.parent, "You Won", f"You Won in {self.parent.tries} tries")
            self.parent.tries = 0
            self.tries.setText(f"Tries: {self.parent.tries}")
            self.set_new_color()
            return True
