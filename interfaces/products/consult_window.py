from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QMessageBox
import sys
import os

path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *


class ConsultWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Buscar')
        self.database_handle = ProductsData()
        
        self.id = QLineEdit()
        self.id.setPlaceholderText("Id") 
        
        self.name = QLineEdit()
        self.name.setPlaceholderText("NOME")
        
        self.pesquisar = QPushButton("Pesquisar", clicked=self.search_product)
        
        self.layout = QHBoxLayout(self)
        self.layout.addWidget(self.id)
        self.layout.addWidget(self.name)
        self.layout.addWidget(self.pesquisar)
        
    
    def search_product(self):
        self.verify_what_user_want_to_search()
    
    def verify_what_user_want_to_search(self):
        id_product = self.id.text()
        name_product = self.name.text()
        
        if id_product and name_product:
            try:
                data = self.database_handle.get_product_by_id_and_name(id_product, name_product)
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao tentar buscar por id e por nome')
            if data:
                print(data)  
            else:
                self.show_dialog('Produto não encontrado')       
        
        elif id_product:
            try:
                data = self.database_handle.get_products_by_id(id_product)
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo id')
            if data:
                print(data)  
            else:
                self.show_dialog('Produto não encontrado')
            
            
        elif name_product:
            try:
                data = self.database_handle.get_products_by_name(name_product)
            except:
                self.show_dialog('erro database ao buscar')
                print('erro ao buscar pelo nome')
            if data:
                print(data)  
            else:
                self.show_dialog('Produto não encontrado')
        
        else:
            self.show_dialog('Coloque uma informação antes de pesquisar!')
                    
                    
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
            

        
    
if __name__ == "__main__":
    app = QApplication([])
    widget = ConsultWindow()
    widget.show()
    sys.exit(app.exec())