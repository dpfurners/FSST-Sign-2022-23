# Two Colums
# Grid Layout
# Menu Bar > Difficulty > Easy, Medium, Hard
# Menu Bar > File > Save, Load, Quit > Skript
# Save > Difficulty, Tries


import sys

from PyQt6.QtWidgets import QApplication

from chooser.page import ChooserPage


app = QApplication(sys.argv)

window = ChooserPage()
window.show()

try:
    app.exec()
except KeyboardInterrupt:
    print("Exiting Program")

