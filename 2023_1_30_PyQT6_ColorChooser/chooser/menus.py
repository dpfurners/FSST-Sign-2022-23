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

        """self.difficulties = {}
        self.easy = self.addAction("Easy")
        self.easy.setToolTip("Easy Difficulty (9 Colors)")
        self.easy.setShortcut("Ctrl+E")
        self.easy.setIcon(QIcon("../check.png"))
        self.easy.setIconVisibleInMenu(False)
        self.medium = self.addAction("Medium")
        self.medium.setToolTip("Medium Difficulty (25 Colors)")
        self.medium.setShortcut("Ctrl+M")
        self.medium.setIcon(QIcon("../check.png"))
        self.hard = self.addAction("Hard")
        self.hard.setToolTip("Hard Difficulty (49 Colors)")
        self.hard.setShortcut("Ctrl+H")
        self.hard.setIcon(QIcon("../check.png"))
        self.hard.setIconVisibleInMenu(False)"""

        """self.easy.triggered.connect(lambda: self.easy_difficulty)
        self.medium.triggered.connect(self.medium_difficulty)
        self.hard.triggered.connect(self.hard_difficulty)"""

    def setup_difficulties(self):
        for difficulty in DIFFICULTIES:
            action = self.addAction(difficulty)
            action.setToolTip(f"{difficulty.capitalize()} Difficulty ({DIFFICULTIES.get(difficulty)} Colors)")
            action.setShortcut(f"Ctrl+{difficulty[0].upper()}")
            action.setIcon(QIcon("assets/check.png"))
            action.setIconVisibleInMenu(False)
            print(difficulty)
            self.difficulties[difficulty] = action
            action.triggered.connect(partial(self.trigger, difficulty))

        print(self.difficulties)
        self.parent.difficulty = list(DIFFICULTIES)[0]

    def trigger(self, difficulty: str):
        for diff in self.difficulties:
            if diff == difficulty:
                self.difficulties.get(diff).setIconVisibleInMenu(True)
                continue
            self.difficulties.get(diff).setIconVisibleInMenu(False)
        self.parent.difficulty = difficulty
        print(self.parent.difficulty)
        self.parent.tries = 0
        self.parent.chooser.setup_colors(self.parent.difficulty)
        self.parent.game.set_new_color()


class FileMenu(QMenu):
    def __init__(self, parent: "ChooserPage"):
        super().__init__("File", parent)
        self.parent: "ChooserPage" = parent

        self.f_dialog = QFileDialog(self.parent)
        self.f_dialog.setNameFilter("Color Chooser Save (*.colc)")

        self.load = self.addAction("Load")
        self.load.setStatusTip("Load the Game")
        self.load.setShortcut("Ctrl+L")
        self.load.triggered.connect(self.load_game)

        self.save = self.addAction("Save")
        self.save.setStatusTip("Save the Game")
        self.save.setShortcut("Ctrl+S")
        self.save.triggered.connect(self.save_game)

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
