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
from add_product_window import *

class ProductsPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Produtos')
        self.setMinimumSize(1024,720)
        #Add the menu options of the program
        self.config_the_toolbar()
        self.label_teste = QLabel()
        self.window_consult = ProductsInfo(self)
        self.window_add = WindowProductAdd(self)
        self.table = QTableView()
        widget = QWidget()
        layout = QHBoxLayout()
        self.label_teste = QLabel()
        layout.addWidget(self.label_teste)
        layout.addWidget(self.table)
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :30px;font-size:18px;margin-top:30px")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(64,64))
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
    
    def config_the_toolbar(self):
        button_consult_product = QAction(QIcon(r'images/filter.png'),"Consultar Produto" ,self)
        button_consult_product.triggered.connect(self.consult_product)
        button_add_product = QAction(QIcon(r'images/plus.png'),"Adicionar Produto" ,self)
        button_add_product.triggered.connect(self.add_product)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        tool.addAction(button_add_product)
        
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
        self.mount_table(list)
        print('main window ',data)
        
    def add_product(self):
        self.window_add.show()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductsPage()
    widget.showMaximized()
    sys.exit(app.exec())