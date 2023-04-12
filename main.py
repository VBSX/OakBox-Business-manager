import sys
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.login import LoginPage
from PySide6.QtWidgets import (
    QApplication
)

app = QApplication([])
login = LoginPage()
login.show()
sys.exit(app.exec())
