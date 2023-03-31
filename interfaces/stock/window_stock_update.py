from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QMessageBox, QMainWindow, QLabel

import sys
import os
from PySide6 import QtCore, QtWidgets, QtGui
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from add_product_database import *


class UpdateStock(QMainWindow):
    def __init__(self,id,nome, quantidade,parent = None):
        super(UpdateStock, self).__init__(parent = parent)
        self.setWindowTitle('Atualizar Quantidade')
        self.database_handle = AddProducts()
        
        self.nome_do_produto = nome
        self.id_product = id
        self.quantidade = quantidade        
        self.mensagem_direcional = QLabel()
        self.mensagem_direcional.setText('Coloque a quantidade a ser adicionada no estoque: ')
        self.Quantidade = QLineEdit()
        self.Quantidade.setPlaceholderText("Quantidade") 
        
        self.Atualizar = QPushButton("Adicionar", clicked=self.update_quantity_database)
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.mensagem_direcional)
        layout.addWidget(self.Quantidade)
        
        layout.addWidget(self.Atualizar)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.data_out = None
    
    def update_quantity_database(self):
        quantidade_para_adicionar_no_estoque = int(self.Quantidade.text())
        print(quantidade_para_adicionar_no_estoque)
        id_product = self.id_product
        quantidade_atual_de_produtos = int(self.quantidade)
        print(quantidade_atual_de_produtos)
        quantidade_final = quantidade_para_adicionar_no_estoque+ quantidade_atual_de_produtos
        print(quantidade_final)
        try:    
            if self.database_handle.update_item_quantity(id_product, quantidade_final, self.nome_do_produto, quantidade_para_adicionar_no_estoque):
                self.show_dialog(f'Estoque atualizado com sucesso, \nQuantidade atualizada de produtos: {quantidade_final}')
        except:
            self.show_dialog('erro database, tente novamente')
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
            

        
    
if __name__ == "__main__":
    app = QApplication([])
    widget = UpdateStock(3, 'salame', 219)
    widget.show()
    sys.exit(app.exec())