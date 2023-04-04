from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QMessageBox, QMainWindow
import sys
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *

class ProductsInfo(QMainWindow):
    def __init__(self,parent = None):
        super(ProductsInfo, self).__init__(parent = parent)
        self.setWindowTitle('Buscar')
        self.database_handle = ProductsData()
        self.setup_ui()
        self.data_out = None

    def setup_ui(self):
        self.id = QLineEdit()
        self.id.setPlaceholderText("Id") 
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("NOME")
        self.pesquisar = QPushButton("Pesquisar", clicked=self.search_product)
        self.name.returnPressed.connect(self.pesquisar.click)
        self.id.returnPressed.connect(self.pesquisar.click)
        widget = QWidget()
        layout = QHBoxLayout()
        
        layout.addWidget(self.id)
        layout.addWidget(self.name)
        layout.addWidget(self.pesquisar)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def search_product(self):
        self.data_out = self.verify_what_user_want_to_search()
    
    def verify_what_user_want_to_search(self):
        id_product = self.id.text()
        name_product = self.name.text()
        data = []
        if id_product and name_product:
            try:
                data = self.database_handle.get_all_info_of_product(id_product, name_product, find_by_id=True, find_by_name=True)
                self.parent().show_products(data)
                 
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao tentar buscar por id e por nome')
            if data:
                print(data)  
                return data
            else:
                self.show_dialog('Produto não encontrado')       
        
        elif id_product:
            try:
                print(id_product)
                data = self.database_handle.get_all_info_of_product(id_product, False, find_by_id=True, find_by_name=True)
                self.parent().show_products(data)
                
                
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo id')
            if data:
                print(data)  
                return data
            else:
                self.show_dialog('Produto não encontrado')
            
        elif name_product:
            try:
                data = self.database_handle.get_all_info_of_product(False, name_product, find_by_id=True, find_by_name=True)
                self.parent().show_products(data)
                
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo nome')
            if data:
                print(data) 
                 
                return data
            else:
                self.show_dialog('Produto não encontrado')
        
        else:
            self.show_dialog('Coloque alguma informação')
        
        
                 
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
     
            
if __name__ == "__main__":
    app = QApplication([])
    widget = ProductsInfo()
    widget.show()
    sys.exit(app.exec())