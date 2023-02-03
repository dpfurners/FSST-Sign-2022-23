import random

from math import sqrt
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QGridLayout, QBoxLayout, QMessageBox, QLabel

from . import DIFFICULTIES, WINDOW_HIGHT
from .widgets import MyColor


class MyChooserLayout(QGridLayout):
    def __init__(self, parent: "ChooserPage", *args, **kwargs):
        """Initialize the Label with list of colors"""
        super().__init__(*args, **kwargs)
        self.parent: "ChooserPage" = parent

        self.colors: list[MyColor] = []

    def setup_colors(self, difficulty):
        """Setup the colors according to the difficulty"""
        self.colors.clear()
        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)

        # Calculate the amount of colors per row/column
        per = int(sqrt(DIFFICULTIES.get(difficulty)))
        size = (int(WINDOW_HIGHT/per), int(WINDOW_HIGHT/per))
        for i in range(DIFFICULTIES.get(difficulty)):
            self.colors.append(MyColor(self.generate_color(), size, self))
            self.addWidget(self.colors[-1], i // per, i % per)

    def generate_color(self):
        """Generate a random color that is not already in the list of colors"""
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        while color in [col.rgb for col in self.colors]:
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        return color


class MyGameLayout(QBoxLayout):
    def __init__(self, parent: "ChooserPage"):
        """Initialize the Game Layout"""
        super().__init__(QBoxLayout.Direction.TopToBottom, parent)

        # Set the target color to None and the parent to the ChooserPage
        self.color = None
        self.parent = parent

        # Initialize the Label for the Target Color and the Tries
        self.target = QLabel("Target Color")
        self.target.setStyleSheet(f"font-size: 30px")
        self.target.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.tries = QLabel(f"Tries: {self.parent.tries}")
        self.tries.setStyleSheet("font-size: 20px")
        self.tries.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.addWidget(self.target)
        self.addWidget(self.tries)

    def set_new_color(self):
        """Set a new color for the target color and update the tries/colors to select from"""
        self.parent.chooser.setup_colors(self.parent.difficulty)
        self.color = random.choice([col.rgb for col in self.parent.chooser.colors])
        self.target.setStyleSheet(f"background-color: rgb{self.color}")
        self.tries.setText(f"Tries: {self.parent.tries}")

    def update_tries(self, color: tuple[int, int, int]):
        """Update the tries and check if the color is the target color"""
        # Player didnt won
        if color != self.color:
            self.parent.tries += 1
            self.tries.setText(f"Tries: {self.parent.tries}")
            return False
        # Player did win
        else:
            self.parent.tries += 1
            self.tries.setText(f"Tries: {self.parent.tries}")
            QMessageBox.information(self.parent, "You Won", f"You Won in {self.parent.tries} tries")
            self.parent.tries = 0
            self.tries.setText(f"Tries: {self.parent.tries}")
            self.set_new_color()
            return True
