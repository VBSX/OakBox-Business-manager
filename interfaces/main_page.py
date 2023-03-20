import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import Qt

from login import LoginPage


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        filter_icon_path = r'images/filter.png'

        #config of the window
        # self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Main Page')
        # self.resize(400, 200)

        
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        button_action_logoff = QAction("logoff", self)
        button_action_logoff.setStatusTip("This is your button")
        button_action_logoff.triggered.connect(self.logoff)
        toolbar.addAction(button_action_logoff)
        
        
        
    def logoff(self):
        self.close()
        self.login = LoginPage()
        self.login.show()
        

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())