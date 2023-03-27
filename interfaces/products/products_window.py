import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QHBoxLayout,QWidget, QPushButton, QToolBar, QLabel,QTableView
)
from PySide6.QtGui import QAction, QIcon
import os
from table_widget import TableWidget
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from login import *
from consult_window import *

class ProductsPage(QMainWindow):
    one = None
    def __init__(self):
        
        super(ProductsPage,self).__init__()
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Produtos')
        self.setMinimumSize(1024,720)
        #Add the menu options of the program
        self.config_the_menubar()
        self.config_the_toolbar()
        self.label_teste = QLabel()
        
        self.window_consult = ConsultWindow(self)
        
        
        self.table = QTableView()
        data = [
          [4, 9, 2],
          [1, 0, 0],
          [3, 5, 0],
          [3, 3, 2],
          [7, 8, 9],
        ]
        

        widget = QWidget()
        layout = QHBoxLayout()
        self.label_teste = QLabel()
        # self.button_products = QPushButton("Produtos", clicked=self.teste)
        # self.button_estoque = QPushButton("Estoque", clicked=self.teste)
        # self.button_caixa = QPushButton("Caixa", clicked=self.teste)
        
        # self.set_icons_and_resize_and_alter_font(self.button_caixa, self.image_test)
        # self.set_icons_and_resize_and_alter_font(self.button_estoque, self.image_test)
        # self.set_icons_and_resize_and_alter_font(self.button_products, self.image_test)
        
        # layout.addWidget(self.button_estoque)
        # layout.addWidget(self.button_products)
        
        layout.addWidget(self.label_teste)
        layout.addWidget(self.table)
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    
    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :30px;font-size:18px;margin-top:30px")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(64,64))
    
    
    
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
        
    
    
    def config_the_toolbar(self):
        button_consult_product = QAction(QIcon(r'images/filter.png'),"Consultar Produto" ,self)
        button_consult_product.triggered.connect(self.consult_product)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        
            
    def consult_product(self):
        self.window_consult.show()
        
    def mount_table(self, data):
        self.model = TableWidget(data, self)
        self.table.setModel(self.model)

        self.setCentralWidget(self.table)
       

    
    def show_products(self, data):
        list = [('id', 'Nome', 'Quantidade', 'Valor Unitário')]
        for d in data:
            
            list.append(d)
        print(list,'aaaa')
        # print(list)
        self.mount_table(list)
        print('main window ',data)

            


        
        
    def teste(self):
        print('teste')
        
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductsPage()
    widget.showMaximized()
    sys.exit(app.exec())