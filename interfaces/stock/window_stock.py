import sys
from PySide6 import  QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, QPushButton, QToolBar, QTableWidget, QTableWidgetItem, QVBoxLayout
)
from PySide6.QtGui import QAction, QIcon
import os
path = os.path.abspath('interfaces/stock')
sys.path.append(path)
from consult_page import *
from window_stock_update import *
path = os.path.abspath('interfaces/')
sys.path.append(path)
from login import *

class StockPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # Config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Estoque')
        self.setMinimumSize(450,320)
        # Add the menu options of the program
        self.config_the_toolbar()
        self.consult_window = ConsultWindow(self)
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(['ID', 'Produto', 'Quantidade', 'Quantidade Atual'])
        self.table.verticalHeader().setVisible(False)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)

        widget = QWidget()
        widget.setLayout(self.layout)
        self.layout.addItem(spacer)
        self.setCentralWidget(widget)
        
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
        
    def update_table(self, data):
        #A função update_table atualiza a tabela com dados passados como parâmetro data.
        # A quantidade de linhas da tabela é ajustada de acordo com a quantidade de itens em data.
        # Em seguida, os valores de cada item são adicionados à tabela, linha por linha e coluna por coluna, 
        # usando o método setItem do QTableWidgetItem. Cada item é convertido para string 
        # usando a função str() antes de ser adicionado à tabela.
        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            for j, item in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(item)))
                
    def show_products(self, data):
        """
        Display the product information in the main window

        Parameters:
            data (list): list of tuples containing the product information

        Returns:
            None
        """
        self.consult_window.close()

        if len(data) > 1:
            str_of_products = self.get_id_and_name_of_list(data)
            self.show_dialog(f'Foi retornado mais de um produto: \n {str_of_products}')
        elif len(data) == 1:
            product_data = data[0]
            self.id_produto = product_data[0]
            self.nome = product_data[1]
            self.quantidade_atual = product_data[3]
            self.update_table(data)
            
            if not hasattr(self, 'button_atualizar_estoque'):
                self.button_atualizar_estoque = QPushButton("Dar entrada no estoque", clicked=self.atualizar_estoque)
                widget = QWidget()
                layout = QVBoxLayout(widget)
                layout.addWidget(self.button_atualizar_estoque)
                self.layout.addWidget(widget)
            else:
                self.button_atualizar_estoque.setText("Dar entrada no estoque")
                
        else:
            self.show_dialog('Nenhum produto encontrado.')

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
