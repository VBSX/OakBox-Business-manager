"""""
 _____             _            _             _  _    _         __ _____      
/  __ \           | |          | |           (_)| |  | |       / /|____ |     
| /  \/  ___    __| |  ___   __| | __      __ _ | |_ | |__    / /     / /     
| |     / _ \  / _` | / _ \ / _` | \ \ /\ / /| || __|| '_ \  < <      \ \     
| \__/\| (_) || (_| ||  __/| (_| |  \ V  V / | || |_ | | | |  \ \ .___/ /     
 \____/ \___/  \__,_| \___| \__,_|   \_/\_/  |_| \__||_| |_|   \_\\____/      
                                                                              
                                                                              
          _____         _     _____                _____  _____  _____  _____ 
   ____  |  _  |       | |   |_   _|              / __  \|  _  |/ __  \|____ |
  / __ \ | | | |  __ _ | | __  | |   _ __    ___  `' / /'| |/' |`' / /'    / /
 / / _` || | | | / _` || |/ /  | |  | '_ \  / __|   / /  |  /| |  / /      \ \
| | (_| |\ \_/ /| (_| ||   <  _| |_ | | | || (__  ./ /___\ |_/ /./ /___.___/ /
 \ \__,_| \___/  \__,_||_|\_\ \___/ |_| |_| \___| \_____/ \___/ \_____/\____/ 
  \____/    
  
                            github.com/vbsx    
                            https://www.oakbox.com.br
                            https://www.linkedin.com/in/oak-borges                                                             
 """"" 
import sys
from PySide6 import  QtWidgets
from PySide6.QtWidgets import ( 
    QWidget,
    QToolBar,
    QTableWidget,
    QTableWidgetItem,
    QVBoxLayout,
    QAbstractItemView
)
from PySide6.QtGui import QAction, QIcon, QColor
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.stock.consult_page import ConsultWindow
from interfaces.stock.window_stock_update import UpdateStock
from interfaces.base_windows.main_window_base import WindowBaseClass

class StockPage(WindowBaseClass):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_icon = r'images/warehouse.png'
        self.consult_window = ConsultWindow(self)
        # Add the menu options of the program
        self.config_the_toolbar()

    def setup_ui(self):
        self.table = QTableWidget()
        self.all_products = self.database_get.get_all_products()
        # Config of the window
        self.icon_set(self.image_icon)
        self.setWindowTitle('Estoque')
        self.setMinimumSize(750, 320)
        
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(
            [
                'ID',
                'Produto',
                'Quantidade',
                'Valor unitario',
                'Unidade medida',
                'Categoria',
                'Status estoque'
                ]
            )
        
        spacer = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.update_table(self.all_products)
        self.table.verticalHeader().setVisible(False)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        widget = QWidget()
        widget.setLayout(self.layout)
        self.layout.addItem(spacer)
        self.setCentralWidget(widget)
        self.icon_set(self.image_icon)
          
    def config_the_toolbar(self):
        button_consult_product = QAction(QIcon(r'images/filter.png'),"Consultar Produto" ,self)
        button_consult_product.triggered.connect(self.consult_product)
        button_add_product = QAction(QIcon(r'images/plus.png'),"Adicionar Produto Ao estoque" ,self)
        button_add_product.triggered.connect(self.product_add_window)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_consult_product)
        tool.addAction(button_add_product)
        
    def consult_product(self):
        self.consult_window.show()
        
    def update_table(self, data):
        #A função update_table atualiza a tabela com dados passados como parâmetro data.
        # A quantidade de linhas da tabela é ajustada de acordo com a quantidade de itens em data.
        # Em seguida, os valores de cada item são adicionados à tabela, linha por linha e coluna por coluna, 
        # usando o método setItem do QTableWidgetItem. Cada item é convertido para string 
        # usando a função str() antes de ser adicionado à tabela.
        # também é realizado a verificação de status de estoque, conforme a quantidade atual do produto.
        # A função config_cell_of_table() é utilizada para configurar a cor de cada célula da tabela e adicionar na tabela. 
        self.table.setRowCount(len(data))
        for i, row in enumerate(data):
            actual_item = 0
            for j, item in enumerate(row):
                actual_item += 1
                if actual_item == 3:
                    stock_quatity = item
                if actual_item<7:
                    self.table.setItem(i, j, QTableWidgetItem(str(item)))
                else:
                    if actual_item == 7:
                        minimum_stock = item
                    elif actual_item == 8:
                        maximum_stock = item
                        
                        status_stock = self.verify_stock_status(stock_quatity, minimum_stock, maximum_stock)
                        
                        if status_stock == 'Baixo':
                            self.config_cell_of_table(i,255,0,0,status_stock)
                        elif status_stock == 'Crítico':
                            self.config_cell_of_table(i,255,11,50,status_stock)
                        elif status_stock == 'Alto':
                            self.config_cell_of_table(i,102,51,0,status_stock)
                            
                        elif status_stock == 'Estável':
                            self.config_cell_of_table(i,185,255,174,status_stock)
                            
                        elif  status_stock == 'Vazio':
                            self.config_cell_of_table(i, 255, 255, 255, status_stock)
                        
                            

    def show_products(self, data):
        # Essa função recebe os dados das janelas "UpdateStock" e "ConsultWindow"
        # e atualiza a tabela com os dados recebidos.
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
        self.update_window_stock = UpdateStock(id, nome, self)
        self.update_window_stock.show()
     
    def product_add_window(self):
        current_index = self.table.currentIndex()
        current_row = current_index.row()
        item_id = self.table.item(current_row, 0)
        item_name = self.table.item(current_row, 1)
        id_clicked = item_id.text()
        nome_clicked = item_name.text()
        self.atualizar_estoque(id_clicked, nome_clicked)
    
    def verify_stock_status(self, stock_quantity, min_stock, max_stock):
        medium_stock = (max_stock + min_stock) / 2

        if stock_quantity == 0:
            return 'Vazio'
        elif stock_quantity > max_stock:
            return 'Alto'
        elif stock_quantity > medium_stock:
            return 'Estável'
        elif stock_quantity < min_stock:
            return 'Crítico'
        elif stock_quantity < medium_stock > min_stock:
            return 'Baixo'

        

    def config_cell_of_table(self, table_index, r_rgb,g_rgb, b_rgb, text_of_cell):
        cell = QTableWidgetItem(str(text_of_cell))
        cell.setBackground(QColor(r_rgb, g_rgb, b_rgb))
        cell.setForeground(QColor(0, 0, 0))
        self.table.setItem(table_index, 6, cell)
        

if  __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = StockPage()
    widget.show()
    sys.exit(app.exec())
