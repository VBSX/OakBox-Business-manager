from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QLabel, QMainWindow, QMessageBox
import sys
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from add_product_database import *
from products_database import *

class WindowProductAdd(QMainWindow):
    def __init__(self, parent = None):
        super(WindowProductAdd, self).__init__(parent = parent)
        self.setWindowTitle('Adicionar Produto')
        self.database_handle_add = AddProducts()
        self.database_handle_consult = ProductsData()
        self.data_out = None
        self.setup_ui()
        
    def setup_ui(self):
        self.message_init = QLabel()
        self.message_init.setText('')
        self.name = QLineEdit()
        self.name.setPlaceholderText("Nome")
        self.add = QPushButton("Adicionar novo produto", clicked=self.send_new_product)
        
        self.valor_unidade = QLineEdit()
        self.valor_unidade.setPlaceholderText("Valor unitario")
        
        self.name.returnPressed.connect(self.add.click)
        self.valor_unidade.returnPressed.connect(self.add.click)
        widget = QWidget()
        layout = QHBoxLayout()
        layout.addWidget(self.name)
        layout.addWidget(self.valor_unidade)
        layout.addWidget(self.add)
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def send_new_product(self):
        nome = self.name.text()
        nome_lower = nome.lower()
        quantidade = '0'
        valor = self.valor_unidade.text()
        if self.verify_in_field_is_not_null():
            if self.verify_if_product_exist_on_database() == False:
                try:
                    self.database_handle_add.add_on_database_new_product(nome_lower, quantidade, valor)
                    self.show_dialog('Produto Adicionado com sucesso!')
                except:
                    self.show_dialog('erro ao adicionar')
                    print('erro ao adicionar na database')
            else:
                self.show_dialog('O produto ja existe!')

    def verify_in_field_is_not_null(self):
        nome = self.name.text()
        valor = self.valor_unidade.text()
        if nome and valor:
            return True
        else:
            self.show_dialog('Prencha os campos antes de continuar')
    
    def verify_if_product_exist_on_database(self):
        nome = self.name.text()
        product_list = self.database_handle_consult.get_product_by_exact_name(nome)
        print(product_list)
        if product_list:
            product = product_list[0][1]
            product_lower = product.lower()
            if product_lower == nome:
                return True
            print(nome, product)
        else:
            return False
        
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
        
if __name__ == "__main__":
    app = QApplication([])
    widget = WindowProductAdd()
    widget.show()
    sys.exit(app.exec())