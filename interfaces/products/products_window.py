from consult_window import *
from add_product_window import *
import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QHBoxLayout,QWidget, QToolBar, QLabel,QTableWidget,QAbstractItemView,QTableWidgetItem
)
from PySide6.QtGui import QAction, QIcon
from table_widget import TableWidget
from product_edit import ProductEditWindow
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))
from login import *
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import ProductsData


class ProductsPage(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_box = r'images/box.png'
        self.window_consult = ProductsInfo(self)
        self.window_add = WindowProductAdd(self)
        #config of the window
        self.setWindowIcon(QtGui.QIcon(self.image_box))
        self.setWindowTitle('Produtos')
        self.setMinimumSize(950,320)
        self.config_the_toolbar()
        self.setup_ui()

    def setup_ui(self):
        #Add the menu options of the program
        
        self.label_teste = QLabel()

        self.table = QTableWidget()
        
        self.table.setColumnCount(9)
        self.table.setHorizontalHeaderLabels(['ID','Codigo produto' ,
                                              'Produto','Valor de custo', 'Valor unitario' ,
                                              'Quantidade','Estoque_minimo','Estoque_maximo',
                                              'Unidade medida', 'Categoria'])
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.database_get = ProductsData()
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
        button_edit_product = QAction(QIcon(r'images/pencil.png'),"Editar Produto" ,self)
        button_edit_product.triggered.connect(self.product_edit_window)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        tool.addAction(button_add_product)
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
            
    def add_product(self):
        self.window_add.show()
    def reset_layout(self):
        # Clear the central widget
        self.centralWidget().setParent(None)
        self.setup_ui()
                
    
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductsPage()
    widget.show()
    sys.exit(app.exec())