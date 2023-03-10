import random

from PyQt6.QtWidgets import QMainWindow, QBoxLayout, QWidget

from .layouts import MyChooserLayout, MyGameLayout
from .menus import DifficultyMenu, FileMenu
from . import WINDOW_HEIGHT, WINDOW_WIDTH, DIFFICULTIES


class ChooserPage(QMainWindow):
    def __init__(self) -> None:
        """Initialize the Login Page"""
        super().__init__()
        self.tries = 0
        self.difficulty = list(DIFFICULTIES)[0]

        # Set the Title and the Size of the Window
        self.setWindowTitle("Color Chooser")
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        # Initialize the Layout and the Main Widget
        self.layout = QBoxLayout(QBoxLayout.Direction.LeftToRight)
        self.chooser = MyChooserLayout(self)
        self.game = MyGameLayout(self)

        # Initialize the Menu Bar
        self.menu = self.menuBar()

        # Initialize the Menus (Difficulty and File)
        self.diff_menu = DifficultyMenu(self)
        self.file_menu = FileMenu(self)

        # Add the Menus to the Menu Bar
        self.menu.addMenu(self.file_menu)
        self.menu.addMenu(self.diff_menu)

        # Add the Layouts to the Main Layout
        self.layout.addLayout(self.chooser)
        self.layout.addLayout(self.game)
        self.main_widget = QWidget()

        self.chooser.setup_colors(self.difficulty)

        # Set the Layout to the Main Widget and set the Main Widget as the Central Widget
        self.main_widget.setLayout(self.layout)
        self.setCentralWidget(self.main_widget)
