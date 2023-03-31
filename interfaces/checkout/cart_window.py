from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QListWidget, QPushButton, QLineEdit, QListWidgetItem, QLabel, QMessageBox
import sys
import os

path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *


class CartWidget(QMainWindow):
    def __init__(self, items, parent = None):
        super().__init__(parent = parent)
        self.items = items
        self.line_edits = []
        self.database_get = ProductsData()
        self.widget = QWidget()
        self.layout_window = QVBoxLayout()
        self.list_widget = QListWidget()
        self.label_valor_total = QLabel()
        self.create_list()
        self.create_remove_button()
        self.create_print_button()
        self.set_layout()
        self.valor_total_do_carrinho = self.obter_valor_total_carrinho(self.items)
        self.label_valor_total.setText(f'O valor Total Do carrinho é de: R$ {str(self.valor_total_do_carrinho)}')
        
        
        
    def create_list(self):
        for item in self.items:
            list_widget_item = QListWidgetItem()
            self.list_widget.addItem(list_widget_item)
            
            label = QLabel(f"Produto (ID: {item[0]}) : {item[1]}, Valor Unitário: {item[3]} ")
            line_edit = QLineEdit()
            line_edit.setStyleSheet("border: 1px solid gray; margin-left: 5px;")
            line_edit.setPlaceholderText('Coloque a quantidade')
            
            hbox_widget = QWidget()
            hbox_layout = QHBoxLayout()

            hbox_widget.setLayout(hbox_layout)
            hbox_layout.addWidget(label)
            hbox_layout.addWidget(line_edit)
            list_widget_item.setSizeHint(hbox_widget.sizeHint())
            self.list_widget.setItemWidget(list_widget_item, hbox_widget)
            self.line_edits.append(line_edit)

    def create_remove_button(self):
        remove_button = QPushButton("Remover Produto")
        remove_button.clicked.connect(self.remove_selected)
        self.layout_window.addWidget(remove_button)

    def create_print_button(self):
        print_button = QPushButton('Efetuar a Venda')
        print_button.clicked.connect(self.efetuar_venda)
        self.layout_window.addWidget(print_button)

    def set_layout(self):
        
        self.layout_window.addWidget(self.list_widget)
        self.layout_window.addWidget(self.label_valor_total)
        self.widget.setLayout(self.layout_window)
        self.setCentralWidget(self.widget)

    def remove_selected(self):
        for item in self.list_widget.selectedItems():
            row = self.list_widget.row(item)
            self.list_widget.takeItem(row)
            line_edit = self.line_edits[row]
            line_edit.setParent(None)
            self.line_edits.remove(line_edit)
            self.items.pop(row)
            self.valor_total_do_carrinho = self.obter_valor_total_carrinho(self.items)
            self.label_valor_total.setText(f'O valor Total Do carrinho é de: R$ {str(self.valor_total_do_carrinho)}')
            
    def efetuar_venda(self):
        produt_has_stock = True
        all_filled = True
        for row in range(self.list_widget.count()):
            item = self.list_widget.item(row)
            line_edit = self.line_edits[row]
            quantidade_informada = line_edit.text()
            if not self.verificar_se_as_quantidades_estão_preenchidas(quantidade_informada):
                self.show_dialog('coloque a quantidade')
                all_filled = False
                break
        if all_filled:
            # for item in self.items:
            #     nome_do_produto = item[1]
            #     id_do_produto = item[0]
            #     if not self.verificar_se_o_produto_tem_no_estoque(nome_do_produto, id_do_produto):
            #         self.show_dialog(f' Produto: {nome_do_produto}\n id {id_do_produto}\n não contem itens no estoque para concluir a transação')
            #         produt_has_stock = False
            #         break
                        
            # if produt_has_stock:
            for row in range(self.list_widget.count()):
                nome_do_produto = self.items[row][1]
                id_do_produto = self.items[row][0]
                item = self.list_widget.item(row)
                line_edit = self.line_edits[row]
                quantidade_informada = line_edit.text()
                print(nome_do_produto,'\n', quantidade_informada)
                if not self.verificar_se_o_produto_tem_no_estoque(nome_do_produto, id_do_produto, quantidade_informada):
                    self.show_dialog(f' Produto: {nome_do_produto}\n id {id_do_produto}\n não contem itens no estoque para concluir a transação')
                    break
             
                    
                    


    def obter_valor_total_carrinho(self, lista):
        print(lista)
        valor_total = 0
        for item in lista:
            
            if self.valor_com_virgula(item[3]):
                
                valor_unitario = float(item[3].replace(',', '.'))
                
                valor_total += valor_unitario
            else:
                valor_unitario = float(item[3])
                valor_total += valor_unitario
            
        return valor_total
        
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)


    def verificar_se_as_quantidades_estão_preenchidas(self, data):
        if data:
            return True

    def valor_com_virgula(self, valor):
        if type(valor) is not int:
            for n in valor:
                if n == ',':
                    return True
        else:
            return False
    
    def verificar_se_o_produto_tem_no_estoque(self, nome_produto, id_produto, quantidade_a_ser_vendida):
  
        data = self.database_get.get_product_quatity(nome_produto, id_produto)
        quantidade = int(data [0][0])
        
        if quantidade >=int(quantidade_a_ser_vendida):
            return True
        

    
    
if __name__ == '__main__':
    items = [(1, "maça",'2', '30,00'), (2, "pera",'2', '40,00'), (3, "Item 3",'3',50)]
    app = QApplication([])
    main_window = CartWidget(items)
    main_window.show()
    app.exec()