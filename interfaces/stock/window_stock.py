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
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import ProductsData

class StockPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.stock_icon = r'images/warehouse.png'
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        # Config of the window
        self.setWindowIcon(QtGui.QIcon(self.stock_icon))
        self.setWindowTitle('Estoque')
        self.setMinimumSize(650,320)
        # Add the menu options of the program
        self.config_the_toolbar()
        self.consult_window = ConsultWindow(self)
        self.table = QTableWidget()
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(['ID', 'Produto', 'Quantidade','Valor unitario' ,'Unidade medida', 'Categoria'])
        self.database_get = ProductsData()
        self.all_products = self.database_get.get_all_products()
        self.update_table(self.all_products)
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
        button_edit_product = QAction(QIcon(r'images/pencil.png'),"Editar Produto" ,self)
        button_edit_product.triggered.connect(self.product_edit_window)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        tool.addAction(button_edit_product)
        
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
            
    def atualizar_estoque(self, id, nome):
        self.update_window_stock = UpdateStock(id,nome,self)
        self.update_window_stock.show()
     
    def product_edit_window(self):
        current_index = self.table.currentIndex()
        current_row = current_index.row()
        item_id = self.table.item(current_row, 0)
        item_name = self.table.item(current_row, 1)
        id_clicked = item_id.text()
        nome_clicked = item_name.text()
        self.atualizar_estoque(id_clicked, nome_clicked)
      
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
    
    
if  __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = StockPage()
    widget.show()
    sys.exit(app.exec())
