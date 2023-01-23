from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QLineEdit, QGridLayout, QPushButton, QWidget, QLabel, QMessageBox

import sys
from email_validator import validate_email, EmailNotValidError


class MyInput(QLineEdit):
    text: str = ""

    def __init__(self, password: bool = False, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.textChanged.connect(self.on_text_changed)
        if password:
            self.setEchoMode(QLineEdit.EchoMode.Password)

    def on_text_changed(self, text):
        self.text = text
        

class MyLabel(QLabel):
    text: str = ""

    def __init__(self, text: str, *args, **kwargs):
        super().__init__(text, *args, **kwargs)

        font = self.font()
        font.setPointSize(18)
        self.setFont(font)


class LoginPage(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("My Login Page")
        self.setFixedSize(400, 200)

        self.layout = QGridLayout()

        self.main_widget = QWidget()

        self.name = MyInput()
        self.name_label = MyLabel("Name")

        self.mail = MyInput()
        self.mail_label = MyLabel("Mail")

        self.password = MyInput(True)
        self.password_label = MyLabel("Password")

        self.password_confirm = MyInput(True)
        self.password_confirm_label = MyLabel("Password (Repetition)")

        self.cancel = QPushButton("Cancel")
        self.cancel.clicked.connect(self._cancel)

        self.accept = QPushButton("OK")
        self.accept.clicked.connect(self._accept)
        
        # Add the Widgets to the Layout with the right position in the grid layout
        # AlignRight is a flag to align the text to the right side 
        self.layout.addWidget(self.name_label, 0, 0, Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.name, 0, 1)
        self.layout.addWidget(self.mail_label, 1, 0, Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.mail, 1, 1)
        self.layout.addWidget(self.password_label, 2, 0, Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.password, 2, 1)
        self.layout.addWidget(self.password_confirm_label, 3, 0, Qt.AlignmentFlag.AlignRight)
        self.layout.addWidget(self.password_confirm, 3, 1)
        self.layout.addWidget(self.cancel, 4, 0)
        self.layout.addWidget(self.accept, 4, 1)

        self.main_widget.setLayout(self.layout)

        self.setCentralWidget(self.main_widget)

    def _cancel(self):
        self.close()

    def _accept(self):
        if self.password.text != self.password_confirm.text:
            wrong_password = QMessageBox()
            wrong_password.setText("Passwords doesn't match")
            wrong_password.setWindowTitle("Login Error")
            wrong_password.exec()
            return

        try:
            validate_email(self.mail.text)
        except EmailNotValidError:
            mail_invalid = QMessageBox()
            mail_invalid.setText("Mail is invalid")
            mail_invalid.setWindowTitle("Login Error")
            mail_invalid.exec()
            return

        done = QMessageBox()
        done.setText("Login Sucessfull \nName: {} \nMail: {}".format(self.name.text, self.mail.text))
        done.setWindowTitle("Finished Login")
        done.exec()
        
        sys.exit()
