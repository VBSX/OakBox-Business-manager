from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QMainWindow, QComboBox, QPushButton,QHBoxLayout,QDialog
from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator, QIntValidator, Qt
import sys
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import *
from add_product_window import *
path = os.path.abspath('interfaces/checkout')
sys.path.append(path)
from dialog_window_confirmation import *


class ProductEditWindow(QMainWindow):
    def __init__(self,id,nome, parent=None):
        super().__init__(parent)
        # Configurando a janela principal
        self.setWindowTitle("Edição de Produto")
        self.setMinimumSize(500,500)
        # Chamando a função para configurar o layout da página
        self.name_of_product = nome
        self.id_of_product = id
        self.database_get = ProductsData()
        self.database_insert = AddProducts()
        
        self.measurement_unit = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
                    self.id_of_product, self.name_of_product,'Unidade_de_medida'
                    ))
        
        self.categoria = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Categoria'
            ))
        
        self.id_to_show = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Id'
            ))
        
        self.codigo_produto = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Codigo_do_produto'
            ))
        
        self.name_product_to_show = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Nome'
            ))
        
        
        self.cost_value = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Valor_de_custo'
            ))
        
        self.unitary_value= str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Valor_unitario'
            ))
        
        self.quantity = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Quantidade'
            ))
        
        self.minimum_stock = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Estoque_minimo'
            ))
        
        self.maximum_stock = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
            self.id_of_product, self.name_of_product,'Estoque_maximo'
            ))
        self.setup_ui()

    def setup_ui(self):
        # Criando um layout vertical para adicionar os labels e line edits
        self.layout = QVBoxLayout()

        # Adicionando o QLabel e QLineEdit para ID
        label_id = QLabel("ID:")
        line_edit_id = QLineEdit()
        line_edit_id.setText(self.id_to_show)
        line_edit_id.setReadOnly(True)
        self.layout.addWidget(label_id)
        self.layout.addWidget(line_edit_id)

        # Adicionando o QLabel e QLineEdit para Codigo Produto
        label_codigo = QLabel("Codigo Produto:")
        self.line_edit_codigo = QLineEdit()
        self.line_edit_codigo.setText(self.codigo_produto)
        self.layout.addWidget(label_codigo)
        self.layout.addWidget(self.line_edit_codigo)

        # Adicionando o QLabel e QLineEdit para Produto
        label_produto = QLabel("Produto:")
        self.line_edit_produto = QLineEdit()
        self.line_edit_produto.setText(self.name_product_to_show)
        self.layout.addWidget(label_produto)
        self.layout.addWidget(self.line_edit_produto)

        
        #adiciona o a parte do valor de custo
        
        layout_valor_custo = QHBoxLayout()
        layout_valor_custo.setSpacing(10)
        layout_valor_custo.setAlignment(Qt.AlignLeft)
        # Criar um QLineEdit para o valor unitário
        label_valor_custo = QLabel("Valor de Custo:")
        self.line_edit_valor_custo = QLineEdit()

        # Criar um QLabel para o sulfixo
        label_valor_custo_suffix = QLabel("R$")

        # Criar um QDoubleValidator para validar o input do usuário
        validator = QDoubleValidator()
        validator.setDecimals(2)
        validator.setNotation(QDoubleValidator.StandardNotation)

        # Adicionar o validator no QLineEdit
        self.line_edit_valor_custo.setValidator(validator)
        self.line_edit_valor_custo.setFixedWidth(100)
        self.line_edit_valor_custo.setText(self.cost_value)
        
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_valor_custo.addWidget(label_valor_custo, 0, Qt.AlignLeft)
        
        layout_valor_custo.addWidget(label_valor_custo_suffix, 0, Qt.AlignLeft)
        layout_valor_custo.addWidget(self.line_edit_valor_custo, 0, Qt.AlignLeft)

        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_valor_custo)

        # Criar um QHBoxLayout para adicionar o QLineEdit e o QLabel na mesma linha
        layout_unitario = QHBoxLayout()
        layout_unitario.setSpacing(10)
        layout_unitario.setAlignment(Qt.AlignLeft)
        
        # Criar um QLineEdit para o valor unitário
        label_unitario = QLabel("Valor Unitario:")
        self.line_edit_unitario = QLineEdit()

        # Criar um QLabel para o sulfixo
        label_unitario_suffix = QLabel(" R$")
   
        # Adicionar o validator no QLineEdit
        self.line_edit_unitario.setValidator(validator)
        self.line_edit_unitario.setFixedWidth(100)
        self.line_edit_unitario.setText(self.unitary_value)
        
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_unitario.addWidget(label_unitario, 0, Qt.AlignLeft)
        
        layout_unitario.addWidget(label_unitario_suffix, 0, Qt.AlignLeft)
        layout_unitario.addWidget(self.line_edit_unitario, 0, Qt.AlignLeft)

        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_unitario)

        # Adicionar os widgets restantes na grid layout
        label_quantidade = QLabel("Quantidade:")
        line_edit_quantidade = QLineEdit()
        line_edit_quantidade.setText(self.quantity)
        line_edit_quantidade.setReadOnly(True)
        self.layout.addWidget(label_quantidade)
        self.layout.addWidget(line_edit_quantidade)        

        # Adicionando o QLabel e QLineEdit para Estoque Minimo
        label_minimo = QLabel("Estoque Minimo:")
        self.line_edit_minimo = QLineEdit()
        self.line_edit_minimo.setText(self.minimum_stock)
        self.line_edit_minimo.setValidator(QIntValidator()) 

        self.layout.addWidget(label_minimo)
        self.layout.addWidget(self.line_edit_minimo)

        # Adicionando o QLabel e QLineEdit para Estoque Maximo
        label_maximo = QLabel("Estoque Maximo:")
        self.line_edit_maximo = QLineEdit()
        self.line_edit_maximo.setText(self.maximum_stock)
        self.line_edit_maximo.setValidator(QIntValidator()) 
        self.layout.addWidget(label_maximo)
        self.layout.addWidget(self.line_edit_maximo)
        
        label_unidade = QLabel("Unidade de Medida:")
        self.combo_box_unidade = QComboBox()
        self.combo_box_unidade.addItems([
            self.measurement_unit
            ])
        
        for unity in self.database_get.get_all_unity_of_mesurament_acronym():
            if unity[0] == self.measurement_unit:
                print(unity)
                pass
            else:
              self.combo_box_unidade.addItems(unity) 
               
        self.layout.addWidget(label_unidade)
        self.layout.addWidget(self.combo_box_unidade)

        label_categoria = QLabel("Categoria:")
        self.combo_categoria = QComboBox()
        categoria_atual_maiuscula = self.categoria.upper()
        
        self.combo_categoria.addItems([
            categoria_atual_maiuscula
            ])
        for categoria in self.database_get.get_all_category():
            categoria_maiuscula = categoria[0].upper()
            
            if categoria_maiuscula == categoria_atual_maiuscula:
                pass
            else:
                self.combo_categoria.addItems(categoria)
                
        update_item_button = QPushButton()
        update_item_button.setText('Atualizar')
        update_item_button.clicked.connect(self.atualizar_as_informações_do_produto)

        self.layout.addWidget(label_categoria)
        self.layout.addWidget(self.combo_categoria)
        
        self.layout.addWidget(update_item_button)
        # Criando um widget para conter o layout vertical
        widget = QWidget()
        widget.setLayout(self.layout)

        # Adicionando o widget ao central widget da janela principal
        self.setCentralWidget(widget)


    def atualizar_as_informações_do_produto(self):
        categoria_selecionada_para_verificar = self.combo_categoria.currentText()
        unidade_de_medida_selecionada_para_verificar = self.combo_box_unidade.currentText()
        codigo_do_produto_para_verificar = self.line_edit_codigo.text()
        nome_do_produto_para_verificar = self.line_edit_produto.text()
        valor_de_custo_para_verificar = self.line_edit_valor_custo.text()
        valor_unitario_para_verificar = self.line_edit_unitario.text()
        estoque_minimo_para_verificar = self.line_edit_minimo.text()
        estoque_maximo_para_verificar = self.line_edit_maximo.text()

        categoria_atual_maiuscula = self.categoria.upper()
        
        product_code_changed = [False, None, None, None]
        product_name_changed = [False, None, None, None]
        product_cost_value_changed = [False, None, None, None]
        product_unitary_value_changed = [False, None, None, None]
        product_minimum_stock_changed = [False, None, None, None]
        product_maximum_stock_changed = [False, None, None, None]
        product_measurement_unit_changed = [False, None, None, None]
        product_category_changed = [False, None, None, None]
        
        #Verifica se foi alterado o CODIGO DE BARRAS do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.codigo_produto, codigo_do_produto_para_verificar):
            #não foi alterado
            pass
        else:
            product_code_changed = [
                True,
                self.codigo_produto,
                codigo_do_produto_para_verificar,
                'Codigo_do_produto'
                ]
            
            print('Do alter query CODIGO DE BARRAS')
            
        #Verifica se foi alterado o NOME DO PRODUTO comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.name_product_to_show, nome_do_produto_para_verificar):
            #não foi alterado
            pass
        else:
            product_name_changed = [
                True,
                self.name_product_to_show,
                nome_do_produto_para_verificar,
                'Nome'
                ]
            
            print('Do alter query NOME DO PRODUTO')  
            
        #Verifica se foi alterado o VALOR DE CUSTO comparando o nome inicial com o lineEdit 
        if self.verify_if_has_change_on_informations(self.cost_value, valor_de_custo_para_verificar):
            #não foi alterado
            pass
        else:
            product_cost_value_changed = [
                True,
                self.cost_value,
                valor_de_custo_para_verificar, 
                'Valor_de_custo'
                ]
            
            print('Do alter query VALOR DE CUSTO')  
            
        #Verifica se foi alterado o VALOR UNITARIO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.unitary_value, valor_unitario_para_verificar):
            #não foi alterado
            pass
        else:
            product_unitary_value_changed = [
                True,
                self.unitary_value,
                valor_unitario_para_verificar,
                'Valor_unitario'
                ]
            
            print('Do alter query VALOR UNITARIO')  
            
        #Verifica se foi alterado o ESTOQUE MINIMO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.minimum_stock , estoque_minimo_para_verificar):
            #não foi alterado
            pass
        else:
            product_minimum_stock_changed = [
                True,
                self.minimum_stock,
                estoque_minimo_para_verificar, 
                'Estoque_minimo'
                ]
            
            print('Do alter query ESTOQUE MINIMO') 
            
        #Verifica se foi alterado o ESTOQUE MAXIMO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.maximum_stock ,estoque_maximo_para_verificar ):
            #não foi alterado
            pass
        else:
            product_maximum_stock_changed = [
                True,
                self.maximum_stock,
                estoque_maximo_para_verificar,
                'Estoque_maximo'
                ]
            
            print('Do alter query ESTOQUE MAXIMO')
        
        #Verifica se foi alterado A UNIDADE DE MEDIDA do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.measurement_unit ,unidade_de_medida_selecionada_para_verificar ):
            #não foi alterado
            pass
        else:
            product_measurement_unit_changed = [
                True,
                self.measurement_unit,
                unidade_de_medida_selecionada_para_verificar,
                'Unidade_de_medida'
                ]
            
            print('Do alter query UNIDADE DE MEDIDA')
            
            
        #Verifica se foi alterado A CATEGORIA do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(categoria_atual_maiuscula,categoria_selecionada_para_verificar ):
            #não foi alterado
            pass
        
        
        else:
            product_category_changed = [
                True,
                categoria_atual_maiuscula,
                categoria_selecionada_para_verificar, 
                'Categoria'
                ]
            print('Do alter query CATEGORIA')
        if self.verify_if_minimum_stock_is_less_than_maximum_stock(
            estoque_minimo_para_verificar,
            estoque_maximo_para_verificar):
            if self.verify_if_the_user_want_to_continue_editing_the_itens(
                product_code_changed,
                product_name_changed,
                product_cost_value_changed,
                product_unitary_value_changed,
                product_minimum_stock_changed,
                product_maximum_stock_changed,
                product_measurement_unit_changed,
                product_category_changed
                ) == True:
                if self.update_itens_on_database(
                    product_code_changed,
                    product_name_changed,
                    product_cost_value_changed,
                    product_unitary_value_changed,
                    product_minimum_stock_changed,
                    product_maximum_stock_changed,
                    product_measurement_unit_changed,
                    product_category_changed
                ):  
                    self.show_dialog('Atualizado!')
                    self.parent().reset_layout()
                    self.close()
        else:
            self.show_dialog('O estoque minimo tem que ser menor do que o estoque maximo!')       
                
    
    def verify_if_the_user_want_to_continue_editing_the_itens(
        self,
        product_code_changed,
        product_name_changed,
        product_cost_value_changed,
        product_unitary_value_changed,
        product_minimum_stock_changed,
        product_maximum_stock_changed,
        product_measurement_unit_changed,
        product_category_changed ):
        texto_final ='Você deseja alterar os itens atuais pelos que estão abaixo:  '

        list_of_itens =[
            product_code_changed,
            product_name_changed,
            product_cost_value_changed,
            product_unitary_value_changed,
            product_minimum_stock_changed,
            product_maximum_stock_changed,
            product_measurement_unit_changed,
            product_category_changed]

        for item in list_of_itens:
            if item[0] == True:
                item_changed = item[2]
                item_initial_info = item[1]
                texto_final+='\nSem a modificação:'+str(item_initial_info)+'\nCom a modificação: '+str(item_changed)+'\n'
                
        if self.verify_if_has_one_item_edited(
            product_code_changed,
            product_name_changed,
            product_cost_value_changed,
            product_unitary_value_changed,
            product_minimum_stock_changed,
            product_maximum_stock_changed,
            product_measurement_unit_changed,
            product_category_changed):   
                
            tela_de_confirmação = MyDialog(texto_final,'Atualizar Itens',self)
            tela_de_confirmação.show()
            if tela_de_confirmação.exec() == QDialog.Accepted:
                return True
            else:
                return False
        else:
            self.show_dialog('Não há itens para editar')
        
    def verify_if_has_change_on_informations(self,elemento_sem_alteração, elemento_do_produto_alterado):
        if elemento_sem_alteração  == elemento_do_produto_alterado:
            #Not Changed
            return True    

    def verify_if_has_one_item_edited(
        self, 
        product_code_changed,
        product_name_changed,
        product_cost_value_changed,
        product_unitary_value_changed,
        product_minimum_stock_changed,
        product_maximum_stock_changed,
        product_measurement_unit_changed,
        product_category_changed):
        list_itens = [
            product_code_changed,
            product_name_changed,
            product_cost_value_changed,
            product_unitary_value_changed,
            product_minimum_stock_changed,
            product_maximum_stock_changed,
            product_measurement_unit_changed,
            product_category_changed]
        has_item_edited = False
        
        for item in list_itens:
            
            if item[0] == True:
                has_item_edited = True
                break
            
        if has_item_edited == True:
            return True

    def update_itens_on_database(
        self,
        product_code_changed,
        product_name_changed,
        product_cost_value_changed,
        product_unitary_value_changed,
        product_minimum_stock_changed,
        product_maximum_stock_changed,
        product_measurement_unit_changed,
        product_category_changed):
        
        list_of_itens = [
            product_code_changed,
            product_name_changed,
            product_cost_value_changed,
            product_unitary_value_changed,
            product_minimum_stock_changed,
            product_maximum_stock_changed,
            product_measurement_unit_changed,
            product_category_changed]
        
        for item in list_of_itens:
            item_changed_verify = item[0]
            item_info_to_update = item[2]
            item_to_update = item[3]
            if item_changed_verify == True:
                database_return = self.database_insert.update_one_part_of_the_product_information( item_to_update,item_info_to_update, self.id_of_product)
                if database_return != True:
                    self.show_dialog(f'{database_return}')
                    break
        if database_return:
            return True
  
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
    def verify_if_minimum_stock_is_less_than_maximum_stock(self,estoque_minimo,estoque_maximo):
        if int(estoque_minimo) < int(estoque_maximo):
            return True
          
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = ProductEditWindow(1, 'pudim')
    widget.show()
    sys.exit(app.exec())