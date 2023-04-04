from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QMainWindow, QComboBox
from PySide6 import QtWidgets
import sys
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *

class ProductEditWindow(QMainWindow):
    def __init__(self,id,nome, parent=None):
        super().__init__(parent)
        # Configurando a janela principal
        self.setWindowTitle("Edição de Produto")
        self.setMinimumSize(500,500)
        # Chamando a função para configurar o layout da página
        self.name_of_product = nome
        self.id_of_product = id
        self.database_get = ProductsData()
        
        self.setup_ui()

    def setup_ui(self):
        # Criando um layout vertical para adicionar os labels e line edits
        layout = QVBoxLayout()

        # Adicionando o QLabel e QLineEdit para ID
        label_id = QLabel("ID:")
        line_edit_id = QLineEdit()
        line_edit_id.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Id'
            )))
        line_edit_id.setReadOnly(True)
        layout.addWidget(label_id)
        layout.addWidget(line_edit_id)

        # Adicionando o QLabel e QLineEdit para Codigo Produto
        label_codigo = QLabel("Codigo Produto:")
        line_edit_codigo = QLineEdit()
        line_edit_codigo.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Codigo_do_produto'
            )))
        layout.addWidget(label_codigo)
        layout.addWidget(line_edit_codigo)

        # Adicionando o QLabel e QLineEdit para Produto
        label_produto = QLabel("Produto:")
        line_edit_produto = QLineEdit()
        line_edit_produto.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Nome'
            )))
        layout.addWidget(label_produto)
        layout.addWidget(line_edit_produto)

        # Adicionando o QLabel e QLineEdit para Valor de Custo
        label_custo = QLabel("Valor de Custo:")
        line_edit_custo = QLineEdit()
        line_edit_custo.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Valor_de_custo'
            )))
        layout.addWidget(label_custo)
        layout.addWidget(line_edit_custo)

        # Adicionando o QLabel e QLineEdit para Valor Unitario
        label_unitario = QLabel("Valor Unitario:")
        line_edit_unitario = QLineEdit()
        line_edit_unitario.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Valor_unitario'
            )))
        layout.addWidget(label_unitario)
        layout.addWidget(line_edit_unitario)

        # Adicionando o QLabel e QLineEdit para Quantidade
        label_quantidade = QLabel("Quantidade:")
        line_edit_quantidade = QLineEdit()
        line_edit_quantidade.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Quantidade'
            )))
        line_edit_quantidade.setReadOnly(True)
        layout.addWidget(label_quantidade)
        layout.addWidget(line_edit_quantidade)

        # Adicionando o QLabel e QLineEdit para Estoque Minimo
        label_minimo = QLabel("Estoque Minimo:")
        line_edit_minimo = QLineEdit()
        line_edit_minimo.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Estoque_minimo'
            )))
        layout.addWidget(label_minimo)
        layout.addWidget(line_edit_minimo)

        # Adicionando o QLabel e QLineEdit para Estoque Maximo
        label_maximo = QLabel("Estoque Maximo:")
        line_edit_maximo = QLineEdit()
        line_edit_maximo.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Estoque_maximo'
            )))
        layout.addWidget(label_maximo)
        layout.addWidget(line_edit_maximo)

        label_unidade = QLabel("Unidade de Medida:")
        combo_box_unidade = QComboBox()
        combo_box_unidade.addItems([str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Unidade_de_medida'
            )),'cm', 'kg', 'L', 'un'])
        
        layout.addWidget(label_unidade)
        layout.addWidget(combo_box_unidade)
        # Adicionando o QLabel e QLineEdit para Categoria
        label_categoria = QLabel("Categoria:")
        line_edit_categoria = QLineEdit()
        line_edit_categoria.setText(str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Categoria'
            )))
        layout.addWidget(label_categoria)
        layout.addWidget(line_edit_categoria)

        # Criando um widget para conter o layout vertical
        widget = QWidget()
        widget.setLayout(layout)

        # Adicionando o widget ao central widget da janela principal
        self.setCentralWidget(widget)

    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductEditWindow(1, 'pudim')
    widget.show()
    sys.exit(app.exec())