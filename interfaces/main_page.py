import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QHBoxLayout,QWidget, QPushButton
)
from PySide6.QtGui import QAction, QIcon


from login import *


class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Main Page')

        #Add the menu options of the program
        self.config_the_menubar()

           
        
        widget = QWidget()
        layout = QHBoxLayout()
        self.button_products = QPushButton("Produtos", clicked=self.teste)
        self.button_estoque = QPushButton("Estoque", clicked=self.teste)
        self.button_caixa = QPushButton("Caixa", clicked=self.teste)
        
        self.set_icons_and_resize_and_alter_font(self.button_caixa, self.image_test)
        self.set_icons_and_resize_and_alter_font(self.button_estoque, self.image_test)
        self.set_icons_and_resize_and_alter_font(self.button_products, self.image_test)
        
        layout.addWidget(self.button_estoque)
        layout.addWidget(self.button_products)
        layout.addWidget(self.button_caixa)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    
    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :15px;font-size:18px;")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(130,130))
    
    
    def teste(self):
        print('teste')
        
    def logoff(self):
        self.close()
        self.login = LoginPage()
        self.login.show()
        

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)

    def config_the_menubar(self):
            
        button_action_logoff = QAction("logoff", self)
        button_action_logoff.triggered.connect(self.logoff)
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('self.teste')
        log = bar.addMenu('Usuário')
        log.addAction(button_action_logoff)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())