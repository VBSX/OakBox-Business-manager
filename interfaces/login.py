import sys
from PySide6 import QtCore, QtWidgets, QtGui

from main_page import *

class LoginPage(QtWidgets.QWidget):
    def __init__(self):
        super(LoginPage, self).__init__()
        filter_icon_path = r'images/filter.png'
        #config of the window
        self.setStyleSheet("padding :15px;background-color: #00008b;color: #FFFFFF ")
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Logar')
        self.resize(400, 200)
        self.username_input = QtWidgets.QLineEdit()
        self.username_message = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.username_message.setText("Coloque o usuário")
        self.password_input = QtWidgets.QLineEdit()
        self.password_message = QtWidgets.QLabel(alignment=QtCore.Qt.AlignCenter)
        self.password_message.setText("Coloque a senha")
        self.logar = QtWidgets.QPushButton("Logar", clicked=self.login_process)
        #set css on itens
        self.username_input.setStyleSheet("background-color: #FFFFFF;color: #000000")
        self.logar.setStyleSheet("background-color: #008b8b;color: #000000")
        self.username_message.setStyleSheet("background-color: #008b8b;color: #000000")
        self.password_message.setStyleSheet("background-color: #008b8b;color: #000000")
        self.password_input.setStyleSheet("background-color: #FFFFFF;color: #000000")
        #Put the itens  on screen
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.username_message)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_message)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.logar)
    
    def open_main_page(self):
        self.main_page = MainPage()
        
        self.main_page.showMaximized()

    def login_process(self):
        if self.verify_if_field_arent_null() == True:
            if self.verify_credentials() == True:
                self.close()
                self.open_main_page()
            else:
                self.show_dialog('Usuário e senha não está correto')
        else:
            self.show_dialog('Coloque o usuário e a senha antes de continuar!')
                  
    def verify_if_field_arent_null(self):
        user = self.username_input.text()
        password = self.password_input.text()
        if user and password:
            return True
        else:
            return False
        
    def verify_credentials(self):
        user = self.username_input.text()
        password = self.password_input.text()
        # if user == 'admin' and password == '12345':
        #     return True
        if user and password:
            return True        

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    self.widget = LoginPage()
    self.widget.show()
    sys.exit(app.exec())