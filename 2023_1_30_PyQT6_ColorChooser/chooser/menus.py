from functools import partial
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMenu, QFileDialog

from . import DIFFICULTIES


class DifficultyMenu(QMenu):
    def __init__(self, parent: "ChooserPage"):
        super().__init__("Difficulty", parent)
        self.parent: "ChooserPage" = parent

        self.difficulties = {}

        self.setup_difficulties()

    def setup_difficulties(self):
        for index, difficulty in enumerate(DIFFICULTIES, start=1):
            action = self.addAction(difficulty)
            action.setToolTip(f"{difficulty.capitalize()} Difficulty ({DIFFICULTIES.get(difficulty)} Colors)")
            action.setShortcut(f"Ctrl+{index}")
            self.difficulties[difficulty] = action
            action.triggered.connect(partial(self.trigger, difficulty))

        self.parent.difficulty = list(DIFFICULTIES)[0]

    def trigger(self, difficulty: str):
        self.parent.difficulty = difficulty
        self.parent.tries = 0
        self.parent.chooser.setup_colors(self.parent.difficulty)
        self.parent.game.set_new_color()


class FileMenu(QMenu):
    def __init__(self, parent: "ChooserPage"):
        super().__init__("File", parent)
        self.parent: "ChooserPage" = parent

        # Initialize the File Dialog to get the name of the file to save/load
        self.f_dialog = QFileDialog(self.parent)
        self.f_dialog.setNameFilter("Color Chooser Save (*.colc)")

        # Add the Load Action to the File Menu
        self.load = self.addAction("Load")
        self.load.setStatusTip("Load the Game")
        self.load.setShortcut("Ctrl+L")
        self.load.triggered.connect(self.load_game)

        # Add the Save Action to the File Menu
        self.save = self.addAction("Save")
        self.save.setStatusTip("Save the Game")
        self.save.setShortcut("Ctrl+S")
        self.save.triggered.connect(self.save_game)

        # Add the Exit Action to the File Menu
        self.exit = self.addAction("Exit")
        self.exit.setStatusTip("Exit the Application")
        self.exit.setShortcut("Ctrl+Q")
        self.exit.triggered.connect(self.exit_app)

    def load_game(self):
        """Load the Game from a .colc File"""
        file_name, _ = self.f_dialog.getOpenFileName(self, "Load Game", "save.colc", "Color Chooser Save (*.colc)")
        with open(file_name, "r") as file:
            self.parent.difficulty = file.readline().strip()
            self.parent.tries = int(file.readline().strip())
            self.parent.game.tries.setText("Tries: " + str(self.parent.tries))

    def save_game(self):
        """Save the Game to a .colc File"""
        file_name, _ = self.f_dialog.getSaveFileName(self, "Load Game", "save.colc", "Color Chooser Save (*.colc)")
        with open(file_name, "w") as file:
            file.write(f"{self.parent.difficulty}\n{self.parent.tries}")

    def exit_app(self):
        """Exit the Application"""
        self.parent.close()
