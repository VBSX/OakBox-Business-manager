import sys
from PySide6 import  QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, QPushButton, QToolBar, QLabel, QGridLayout
)
from PySide6.QtGui import QAction, QIcon
import os
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from consult_page import *
from window_stock_update import *
from login import *

class StockPage(QMainWindow):
    def __init__(self):
        super(StockPage,self).__init__()
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Estoque')
        # self.setMinimumSize(1024,720)
        #Add the menu options of the program
        self.config_the_menubar()
        self.config_the_toolbar()
        
        self.consult_window = ProductsInfo(self)
        
        self.label_id_description = QLabel()
        self.label_id_description.setText('ID')
             
   
        self.label_id = QLabel()
        self.label_nome_produto = QLabel()
        self.label_nome_produto_description = QLabel()
        self.label_nome_produto_description.setText('PRODUTO')
        
        
        self.label_quantidade = QLabel()
        self.label_quantidade_description = QLabel()
        self.label_quantidade_description.setText('QUANTIDADE')
        
        
        self.label_quantidade_atual = QLabel()
        self.label_quantidade_atual_description = QLabel()
        self.label_quantidade_atual_description.setText('QUANTIDADE ATUAL')
        
        
        self.layout = QGridLayout()
        
        self.layout.addWidget(self.label_id_description, 0,1)
        self.layout.addWidget(self.label_nome_produto_description,0,2)
        self.layout.addWidget(self.label_quantidade_description,0,3)
        self.layout.addWidget(self.label_quantidade_description,0,4)
        self.layout.addWidget(self.label_quantidade_atual_description,0,5)
        
        self.layout.addWidget(self.label_id, 1,1)
        self.layout.addWidget(self.label_nome_produto,1,2)
        self.layout.addWidget(self.label_quantidade,1,3)
        self.layout.addWidget(self.label_quantidade,1,4)
        self.layout.addWidget(self.label_quantidade_atual,1,5)
        self.layout.rowStretch(2)
       
        widget = QWidget()
        widget.setLayout(self.layout)
        self.setCentralWidget(widget)  

    def config_the_menubar(self):
            
        button_action_logoff = QAction("logoff", self)
        button_action_logoff.triggered.connect(self.logoff)
        
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('self.teste')
        log = bar.addMenu('Usuário')
        log.addAction(button_action_logoff)
        
    def logoff(self):
        self.close()
        self.login = LoginPage()
        self.login.show()
    
    def config_the_toolbar(self):
        button_consult_product = QAction(QIcon(r'images/filter.png'),"Consultar Produto" ,self)
        button_consult_product.triggered.connect(self.consult_product)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        
        
    def consult_product(self):
        self.consult_window.show()
    
    def show_products(self, data):
        str_of_products = self.get_id_and_name_of_list(data)
    
        number_of_products_retorned = self.cont_products(data)
        
        if number_of_products_retorned >1:
            self.show_dialog(f'Foi retornado mais de um produto: \n {str_of_products}')
            
            
        else:

            print(data[0][1])
            self.id_produto = data[0][0]
            self.nome = data[0][1]
            quantidade = data[0][2]
            self.quantidade_atual = data[0][3]
            self.label_id.setText(str(self.id_produto))
            self.label_nome_produto.setText(str(self.nome))
            self.label_quantidade.setText(str(quantidade))
            self.label_quantidade_atual.setText(str(self.quantidade_atual))
            
            self.button_atualizar_estoque = QPushButton("Dar entrada no estoque", clicked=self.atualizar_estoque)
            self.layout.addWidget(self.button_atualizar_estoque, 2,5)

        
    def cont_products(self, list):
        number_of_products = 0
        for l in list:
            number_of_products += 1
        
        return number_of_products
    
    def get_id_and_name_of_list(self, list):
        string = ''
        for product in list:
            id_prod = str(product[0])
            name_prod = str(product[1])
            string = string+ '\nid: '+ id_prod+'\nnome: '+ name_prod +'\n'

        return string
            
    def atualizar_estoque(self):
        self.update_window_stock = UpdateStock(self.id_produto,self.nome,self.quantidade_atual,self)
        self.update_window_stock.show()
            
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
   
if  __name__ == "__main__":
    
    app = QtWidgets.QApplication([])
    widget = StockPage()
    widget.show()
    sys.exit(app.exec())