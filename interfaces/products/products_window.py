import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import (
    QHBoxLayout,
    QWidget,
    QToolBar,
    QLabel,
    QTableWidget,
    QAbstractItemView,
    QTableWidgetItem
)
from PySide6.QtGui import QAction, QIcon
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.products.consult_window import *
from interfaces.products.add_product_window import *
from interfaces.products.table_widget import TableWidget
from interfaces.products.product_edit import ProductEditWindow
from interfaces.base_windows.main_window_base import WindowBaseClass

class ProductsPage(WindowBaseClass):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_icon = r'images/box.png'
        self.window_consult = ProductsInfo(self)
        self.window_add = WindowProductAdd(self)
        self.config_the_toolbar()

    def setup_ui(self):
        #config of the window
        self.setWindowTitle('Produtos')
        self.setMinimumSize(950,320)
        self.icon_set(self.image_icon)
        #Add the menu options of the program
        self.label_teste = QLabel()
        self.table = QTableWidget()
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['ID','Codigo produto' ,
                                              'Produto','Valor de custo', 'Valor unitario' ,
                                              'Quantidade','Estoque_minimo','Estoque_maximo',
                                              'Unidade medida', 'Categoria'])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.all_products = self.database_get.get_all_info_of_all_products()        
        self.update_table(self.all_products)
        self.table.verticalHeader().setVisible(False)
        widget = QWidget()
        layout = QHBoxLayout()
        self.label_teste = QLabel()
        layout.addWidget(self.label_teste)
        layout.addWidget(self.table)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
 

    def config_the_toolbar(self):
        button_consult_product = QAction(QIcon(r'images/filter.png'),"Consultar Produto" ,self)
        button_consult_product.triggered.connect(self.consult_product)
        button_add_product = QAction(QIcon(r'images/plus.png'),"Adicionar Produto" ,self)
        button_add_product.triggered.connect(self.add_product)
        button_edit_product = QAction(QIcon(r'images/pencil.png'),"Editar Produto" ,self)
        button_edit_product.triggered.connect(self.product_edit_window)
        self.button_remove_item = QAction(QIcon(r'images/delete.png'),'Remover Produto' ,self)
        self.button_remove_item.triggered.connect(self.product_remove)
        
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        tool.addAction(button_add_product)
        tool.addAction(self.button_remove_item)
        tool.addAction(button_edit_product)
        
    def consult_product(self):
        self.window_consult.show()
    
    def mount_table(self, data):
        self.model = TableWidget(data, self)
        self.table.setModel(self.model)
        self.setCentralWidget(self.table)

    def show_products(self, data):
        self.window_consult.close()
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
            
    def get_id_and_name_of_list(self, list):
        string = ''
        for product in list:
            id_prod = str(product[0])
            name_prod = str(product[1])
            string = string+ '\nid: '+ id_prod+'\nnome: '+ name_prod +'\n'
        return string
    

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
                
    def product_edit_window(self):
        current_index = self.table.currentIndex()
        current_row = current_index.row()
        item_id = self.table.item(current_row, 0)
        item_name = self.table.item(current_row, 2)
        id_clicked = item_id.text()
        nome_clicked = item_name.text()
        self.editar_produto_window = ProductEditWindow(id_clicked, nome_clicked,self)
        self.editar_produto_window.show()
        self.reset_layout()
    
    def product_remove(self):
        current_index = self.table.currentIndex()
        current_row = current_index.row()
        item_id = self.table.item(current_row, 0)
        item_name = self.table.item(current_row, 2)
        id_clicked = item_id.text()
        nome_clicked = item_name.text()      
        if self.user_verify_continue_to_delete(nome_clicked): 
            
            database_return = self.database_insert.delete_product(
                nome_clicked,  id_clicked)
            
            if database_return:
                self.show_dialog(f'Item "{nome_clicked}" removido com sucesso.\nID: "{id_clicked}"')
                self.reset_layout()        
            else:
                self.show_dialog(f'erro:\n {database_return}')  
        
    def add_product(self):
        self.window_add.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductsPage()
    widget.show()
    sys.exit(app.exec())