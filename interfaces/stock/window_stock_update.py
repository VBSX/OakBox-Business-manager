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
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QLineEdit,QApplication,QMessageBox, QMainWindow, QLabel,QVBoxLayout
from PySide6 import QtGui
from PySide6.QtGui import QIntValidator
import sys
import os
path = os.path.abspath('./')
sys.path.append(path)
from database.database_manager.add_product_database import AddProducts       
from database.database_manager.products_database import ProductsData

class UpdateStock(QMainWindow):
    def __init__(self,id,nome,parent = None):
        super(UpdateStock, self).__init__(parent = parent)
        self.setWindowTitle('Entrada Estoque')
        self.stock_icon = r'images/warehouse.png'
        self.setWindowIcon(QtGui.QIcon(self.stock_icon))
        self.database_handle = AddProducts()
        self.database_get = ProductsData()
        self.nome_do_produto = nome
        self.id_product = id
        
        self.setup_ui()

    def setup_ui(self):
        self.quantidade_no_banco = self.database_get.get_product_quatity(self.nome_do_produto,self.id_product)
        self.mensagem_direcional = QLabel()
        self.mensagem_direcional.setText('Coloque a quantidade a ser adicionada no estoque: ')
        self.quantidade_a_adicionar = QLineEdit()
        # self.quantidade_a_adicionar.setValidator(QIntValidator()) 
        validator = QIntValidator()
        validator.setBottom(1)  # Define o limite para que não seja permitido negativos
        self.quantidade_a_adicionar.setValidator(validator)

        self.quantidade_a_adicionar.setPlaceholderText("Quantidade") 
        self.quantidade_a_adicionar.editingFinished.connect(self.atualizar_quantidade_final)

        self.quantidade_atual_label = QLabel("Quantidade Atual:")
        self.quantidade_atual_edit = QLineEdit(f'{self.quantidade_no_banco}')
        self.quantidade_atual_edit.setReadOnly(True)

        self.quantidade_final_label = QLabel("Quantidade Final:")
        self.quantidade_final_edit = QLineEdit()
        self.quantidade_final_edit.setReadOnly(True)

        self.Atualizar = QPushButton("Adicionar", clicked=self.update_quantity_database)
        self.valor_unitario = self.database_get.get_some_data_by_id_and_name_from_products_table(self.id_product, self.nome_do_produto,'Valor_unitario')
        self.unidade_medida = self.database_get.get_some_data_by_id_and_name_from_products_table(self.id_product, self.nome_do_produto,'Unidade_de_medida')
        self.categoria = self.database_get.get_some_data_by_id_and_name_from_products_table(self.id_product, self.nome_do_produto,'Categoria')

        # Add labels and line edits for id, name, unit price, unit of measurement, and category
        self.id_label = QLabel("ID:")
        self.id_edit = QLineEdit(str(self.id_product))
        self.id_edit.setReadOnly(True)

        self.nome_label = QLabel("Nome:")
        self.nome_edit = QLineEdit(self.nome_do_produto)
        self.nome_edit.setReadOnly(True)
        
        self.valor_unitario_label = QLabel("Valor Unitário:")
        self.valor_unitario_edit = QLineEdit(f'R$ {self.valor_unitario}')
        self.valor_unitario_edit.setReadOnly(True)

        self.unidade_medida_label = QLabel("Unidade de Medida:")
        self.unidade_medida_edit = QLineEdit(self.unidade_medida)
        self.unidade_medida_edit.setReadOnly(True)
        
        self.categoria_label = QLabel("Categoria:")
        self.categoria_edit = QLineEdit(self.categoria)
        self.categoria_edit.setReadOnly(True)

        # Add labels and line edits to the layout
        widget = QWidget()
        layout = QVBoxLayout()

        layout.addWidget(self.id_label)
        layout.addWidget(self.id_edit)

        layout.addWidget(self.nome_label)
        layout.addWidget(self.nome_edit)

        layout.addWidget(self.valor_unitario_label)
        layout.addWidget(self.valor_unitario_edit)

        layout.addWidget(self.unidade_medida_label)
        layout.addWidget(self.unidade_medida_edit)
        
        layout.addWidget(self.quantidade_atual_label)
        layout.addWidget(self.quantidade_atual_edit)
        layout.addWidget(self.categoria_label)
        layout.addWidget(self.categoria_edit)

        layout.addWidget(self.mensagem_direcional)
        layout.addWidget(self.quantidade_a_adicionar)


        layout.addWidget(self.Atualizar)


        layout.addWidget(self.quantidade_final_label)
        layout.addWidget(self.quantidade_final_edit)
        
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        
    def update_quantity_database(self):
        quantidade_para_adicionar_no_estoque = int(self.quantidade_a_adicionar.text())
        print(quantidade_para_adicionar_no_estoque)
        id_product = self.id_product
        quantidade_atual_de_produtos = self.database_get.get_product_quatity(self.nome_do_produto,self.id_product)
        print(quantidade_atual_de_produtos)
        quantidade_final = quantidade_para_adicionar_no_estoque+ quantidade_atual_de_produtos
        print(quantidade_final)
        
        try:    
            if self.database_handle.update_item_quantity(id_product, quantidade_final, self.nome_do_produto, quantidade_para_adicionar_no_estoque):
                self.show_dialog(f'Estoque atualizado com sucesso, \nQuantidade atualizada de produtos: {quantidade_final}')
                self.reset_layout()
                self.parent().show_products(self.database_get.get_product_by_id_and_name(self.id_product, self.nome_do_produto))
        except:
            self.show_dialog('erro database, tente novamente')
    
    
    
    def atualizar_quantidade_final(self):
        quantidade_final = int(self.quantidade_a_adicionar.text())+ self.quantidade_no_banco
        self.quantidade_final_edit.setText(str(quantidade_final))
        
    def reset_layout(self):
        # Clear the central widget
        self.centralWidget().setParent(None)
        self.setup_ui()
        
        
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
if __name__ == "__main__":
    app = QApplication([])
    widget = UpdateStock(2, 'salame')
    widget.show()
    sys.exit(app.exec())