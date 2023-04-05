from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, 
    QPushButton, QLineEdit, QListWidgetItem, QLabel, QMessageBox, 
)
from PySide6.QtCore import Qt
import sys
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *
from add_product_database import *
from dialog_window_confirmation import *

class CartWidget(QMainWindow):
    def __init__(self, items, parent = None):
        super().__init__(parent = parent)
        self.resize(1024,720)
        self.items = items
        self.line_edits = []
        self.database_get = ProductsData()
        self.database_insert = AddProducts()
        self.widget = QWidget()
        self.layout_window = QVBoxLayout()
        self.list_widget = QListWidget()
        self.label_valor_total = QLabel()
        self.create_list()
        self.create_remove_button()
        self.create_finish_button()
        self.set_layout()
        self.valor_total_do_carrinho = self.obter_valor_total_carrinho()
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
        remove_button.setMaximumWidth(150)  # Define a largura máxima do botão como 150 pixels
        self.layout_window.addWidget(remove_button, 0, Qt.AlignHCenter)  # Adiciona o botão no centro da janela
      
    def create_finish_button(self):
        finish_sell_button = QPushButton('Efetuar a Venda')
        finish_sell_button.clicked.connect(self.efetuar_venda)
        finish_sell_button.setMaximumWidth(150)  # Define a largura máxima do botão como 150 pixels
        self.layout_window.addWidget(finish_sell_button, 0, Qt.AlignHCenter)  # Adiciona o botão no centro da janela
      
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
            self.valor_total_do_carrinho = self.obter_valor_total_carrinho()
            self.label_valor_total.setText(f'O valor Total Do carrinho é de: R$ {str(self.valor_total_do_carrinho)}')
            
    def efetuar_venda(self):
        has_stock = True
        all_filled = True
        has_product = self.verificar_se_tem_produto_adicionado()
        if has_product:
            for row in range(self.list_widget.count()):
                line_edit = self.line_edits[row]
                quantidade_informada = line_edit.text()
                if not self.verificar_se_as_quantidades_estao_preenchidas(quantidade_informada):
                    self.show_dialog('coloque a quantidade')
                    all_filled = False
                    break
            if all_filled:
                for row in range(self.list_widget.count()):
                    nome_do_produto = self.items[row][1]
                    id_do_produto = self.items[row][0]
                    line_edit = self.line_edits[row]
                    quantidade_informada = line_edit.text()
                    print(nome_do_produto,'\n', quantidade_informada)
                    if not self.verificar_se_o_produto_tem_no_estoque(nome_do_produto, id_do_produto, quantidade_informada):
                        self.show_dialog(f' Produto: {nome_do_produto}\n ID: {id_do_produto}\n '
                                        'não contem itens no suficiente estoque para concluir a transação!')
                        has_stock = False
                        break
                if has_stock:    
                    if self.verificar_se_deseja_concluir_a_venda():
                        self.finalizar_venda()
        else:
            self.show_dialog('Adicione um produto antes de continuar')
 
    def verificar_se_deseja_concluir_a_venda(self):
        quantidade_produtos_no_carrinho = self.obter_quantidade_total_de_itens_que_serao_comprados()
        valor_carrinho = self.obter_valor_total_carrinho()
        mensagem = f'Valor total do carrinho: R$ {valor_carrinho}\nQuantidade de itens no carrinho: {quantidade_produtos_no_carrinho}\nDeseja Finalizar a venda?'
        dialog = MyDialog(mensagem,'Concluir Venda',self)
        if dialog.exec() == QDialog.Accepted:
            return True
        else:
            return False
                
    def obter_valor_total_carrinho(self):
        valor_total = float(0)
        for row in range(self.list_widget.count()):
            valor_unitario = self.items[row][3]
            line_edit = self.line_edits[row]
            quantidade_informada = line_edit.text()
            if self.valor_com_virgula(valor_unitario):
                valor_unitario_replaced = float(valor_unitario.replace(',', '.'))
                if quantidade_informada != '':
                    valor_total += valor_unitario_replaced * float(quantidade_informada)
                else:
                    pass
            else:
                valor_unitario_replaced = float(valor_unitario)
                if quantidade_informada != '':
                    valor_total += valor_unitario_replaced * float(quantidade_informada)
                else:
                    pass
            
        return valor_total
    
    def obter_quantidade_total_de_itens_que_serao_comprados(self):
        quantidade_total = 0
        for row in range(self.list_widget.count()):
            line_edit = self.line_edits[row]
            quantidade_informada = line_edit.text()
            if quantidade_informada =='':
                pass
            else:
                quantidade_total +=int(quantidade_informada)
        return quantidade_total
    
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)

    def verificar_se_as_quantidades_estao_preenchidas(self, data):
        if data:
            return True

    def valor_com_virgula(self, valor):
        if type(valor) != int:
            for n in valor:
                if n == ',':
                    return True
        else:
            return False
    def verificar_se_tem_produto_adicionado(self):
        if self.list_widget.count():
            return True
    def verificar_se_o_produto_tem_no_estoque(self, nome_produto, id_produto, quantidade_a_ser_vendida):
        data = self.database_get.get_product_quatity(nome_produto, id_produto)
        quantidade_do_estoque = int(data [0][0])
        if quantidade_do_estoque >=int(quantidade_a_ser_vendida):
            return True
                
    def finalizar_venda(self):
        self.atualizar_estoques()
        self.lancar_venda_concluida()
        self.limpar_widget()
        self.show_dialog('Venda lançada com sucesso!')
    
    def atualizar_estoques(self):
        for row in range(self.list_widget.count()):
            line_edit = self.line_edits[row]
            quantidade_informada = line_edit.text()
            nome_do_produto = self.items[row][1]
            id_do_produto = self.items[row][0]
            data = self.database_get.get_product_quatity(nome_do_produto, id_do_produto)
            
            quantidade_que_existe_atualmente_no_estoque = int(data[0][0])
            quantidade_atualizada_para_o_banco = quantidade_que_existe_atualmente_no_estoque - int(quantidade_informada) 
            print('quantidade no estoque ', quantidade_que_existe_atualmente_no_estoque, 
                  'quantidade atualizada para o banco', quantidade_atualizada_para_o_banco, 
                  'quantidade informada' ,
                  quantidade_informada)
            self.database_insert.update_stock(id_do_produto, quantidade_atualizada_para_o_banco, nome_do_produto)
        
    def lancar_venda_concluida(self):
        for row in range(self.list_widget.count()):
            line_edit = self.line_edits[row]
            quantidade_vendida = line_edit.text()
            nome_do_produto = self.items[row][1]
            id_do_produto = self.items[row][0]
            valor_unitario = self.items[row][3]
            if self.valor_com_virgula(valor_unitario):
                
                valor_unitario_replaced = float(valor_unitario.replace(',', '.'))
                valor_venda = valor_unitario_replaced * float(quantidade_vendida)
            else:
                valor_unitario_replaced = float(valor_unitario)   
                valor_venda = valor_unitario_replaced * int(quantidade_vendida)
            self.database_insert.insert_produtos_vendidos(id_do_produto, nome_do_produto, quantidade_vendida, valor_unitario, valor_venda)
   
    def limpar_widget(self):
        for row in range(self.list_widget.count()):
            # item = self.list_widget.item(row)
            self.list_widget.takeItem(0)
            line_edit = self.line_edits[0]
            print(line_edit)
            line_edit.setParent(None)
            self.line_edits.remove(line_edit)
            self.items.pop(0)
        self.label_valor_total.setText(f'O valor Total Do carrinho é de: R$ 0')
       
if __name__ == '__main__':
    items = [(1, "maça",'2', '30,00'), (19, 'batata', 0, 10), (17, 'Salame', 0, 1)]
    app = QApplication([])
    main_window = CartWidget(items)
    main_window.show()
    app.exec()