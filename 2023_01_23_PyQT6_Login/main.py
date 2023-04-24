import sys

from PyQt6.QtWidgets import QApplication

from login import LoginPage


app = QApplication(sys.argv)

window = LoginPage()
window.show()

try:
    app.exec()
except KeyboardInterrupt:
    print("Exiting Program")
