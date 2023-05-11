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
        self.setWindowTitle('Estoque')
        self.setMinimumSize(750,320)
        self.icon_set(self.image_icon)
        
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
                        
                        status_stock = self.verify_status_of_actual_stock(stock_quatity, minimum_stock, maximum_stock)
                        if status_stock == 'Baixo':
                            text = QTableWidgetItem(str(status_stock))
                            text.setBackground(QColor(255, 0, 0))
                            self.table.setItem(i, 6, text)
                        elif status_stock == 'Alto':
                            text = QTableWidgetItem(str(status_stock))
                            text.setBackground(QColor(102, 51, 0))
                            self.table.setItem(i, 6, text)
                        elif status_stock == 'Estável':
                            text = QTableWidgetItem(str(status_stock))
                            text.setBackground(QColor(185, 255, 174))
                            self.table.setItem(i, 6, text)
                        elif  status_stock == 'Vazio':
                            text = QTableWidgetItem(str(status_stock))
                            text.setBackground(QColor(255, 255, 255))
                            self.table.setItem(i, 6, text)

                    
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
     
    def product_add_window(self):
        current_index = self.table.currentIndex()
        current_row = current_index.row()
        item_id = self.table.item(current_row, 0)
        item_name = self.table.item(current_row, 1)
        id_clicked = item_id.text()
        nome_clicked = item_name.text()
        self.atualizar_estoque(id_clicked, nome_clicked)
    
    def verify_status_of_actual_stock(self,stock_quantity, minimum_stock, maximum_stock):
        if stock_quantity > maximum_stock:
            status_stock = 'Alto'
        elif stock_quantity > (maximum_stock + minimum_stock)/2 and stock_quantity < maximum_stock and stock_quantity !=0: 
            status_stock = 'Estável'
        elif stock_quantity < (
            maximum_stock + minimum_stock
            )/2 and stock_quantity < maximum_stock and stock_quantity !=0 or stock_quantity < minimum_stock and stock_quantity !=0:
            status_stock = 'Baixo'      
        elif stock_quantity == 0:
            status_stock = 'Vazio'  
        print(status_stock)
        return status_stock

if  __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = StockPage()
    widget.show()
    sys.exit(app.exec())
