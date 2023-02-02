from PyQt6.QtWidgets import QPushButton


class MyColor(QPushButton):
    def __init__(self, color: tuple[int, int, int], size: tuple[int, int], parent: "MyColorLayout", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parent: "MyChooserLayout" = parent
        self.rgb = color

        self.setFixedSize(*size)
        self.setStyleSheet(f"background-color: rgb{color}")

        self.clicked.connect(self.pressed)

    def pressed(self):
        self.parent.parent.game.update_tries(self.rgb)

