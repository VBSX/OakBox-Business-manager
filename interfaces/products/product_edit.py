from PySide6.QtWidgets import QLabel, QLineEdit, QVBoxLayout, QWidget, QMainWindow, QComboBox, QPushButton,QHBoxLayout,QDialog
from PySide6 import QtWidgets
from PySide6.QtGui import QDoubleValidator, QIntValidator, Qt
from PySide6 import QtCore
import sys
import os
path = os.path.abspath('./')
sys.path.append(path)
from database.database_manager.products_database import ProductsData
from interfaces.checkout.dialog_window_confirmation import MyDialog
from database.database_manager.add_product_database import AddProducts

class ProductEditWindow(QMainWindow):
    def __init__(self,id,nome, parent=None):
        super().__init__(parent)
        
        # Configurando a janela principal
        self.setWindowModality(QtCore.Qt.ApplicationModal)
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
        
        self.code_bar_of_product = str(self.database_get.get_some_data_by_id_and_name_from_products_table(
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
        label_code_bar = QLabel("Codigo Produto:")
        self.line_edit_code_bar = QLineEdit()
        self.line_edit_code_bar.setText(self.code_bar_of_product)
        self.layout.addWidget(label_code_bar)
        self.layout.addWidget(self.line_edit_code_bar)

        # Adicionando o QLabel e QLineEdit para Produto
        label_product_name = QLabel("Produto:")
        self.line_edit_product_name = QLineEdit()
        self.line_edit_product_name.setText(self.name_product_to_show)
        self.layout.addWidget(label_product_name)
        self.layout.addWidget(self.line_edit_product_name)

        
        #adiciona o a parte do valor de custo
        
        layout_cost_value = QHBoxLayout()
        layout_cost_value.setSpacing(10)
        layout_cost_value.setAlignment(Qt.AlignLeft)
        # Criar um QLineEdit para o valor unitário
        label_cost_value = QLabel("Valor de Custo:")
        self.line_edit_cost_value = QLineEdit()

        # Criar um QLabel para o sulfixo
        label_cost_value_suffix = QLabel("R$")

        # Criar um QDoubleValidator para validar o input do usuário
        validator_double = QDoubleValidator()
               
        validator_double.setBottom(1)  # Define o limite para que não seja permitido negativos

        validator_double.setDecimals(2)
        validator_double.setNotation(QDoubleValidator.StandardNotation)

        #Validador para numeros inteiros e positivos
        
        validator_int = QIntValidator()
        validator_int.setBottom(1)
        
        # Adicionar o validator no QLineEdit
        self.line_edit_cost_value.setValidator(validator_double)
        self.line_edit_cost_value.setFixedWidth(100)
        self.line_edit_cost_value.setText(self.cost_value)
        
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_cost_value.addWidget(label_cost_value, 0, Qt.AlignLeft)
        
        layout_cost_value.addWidget(label_cost_value_suffix, 0, Qt.AlignLeft)
        layout_cost_value.addWidget(self.line_edit_cost_value, 0, Qt.AlignLeft)

        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_cost_value)

        # Criar um QHBoxLayout para adicionar o QLineEdit e o QLabel na mesma linha
        layout_unitary_value = QHBoxLayout()
        layout_unitary_value.setSpacing(10)
        layout_unitary_value.setAlignment(Qt.AlignLeft)
        
        # Criar um QLineEdit para o valor unitário
        label_unitary = QLabel("Valor Unitario:")
        self.line_edit_unitary_value = QLineEdit()

        # Criar um QLabel para o sulfixo
        label_unitario_suffix = QLabel(" R$")
   
        # Adicionar o validator no QLineEdit
        self.line_edit_unitary_value.setValidator(validator_double)
        self.line_edit_unitary_value.setFixedWidth(100)
        self.line_edit_unitary_value.setText(self.unitary_value)
        
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_unitary_value.addWidget(label_unitary, 0, Qt.AlignLeft)
        
        layout_unitary_value.addWidget(label_unitario_suffix, 0, Qt.AlignLeft)
        layout_unitary_value.addWidget(self.line_edit_unitary_value, 0, Qt.AlignLeft)

        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_unitary_value)

        # Adicionar os widgets restantes na grid layout
        label_quantity = QLabel("Quantidade:")
        line_edit_quantity_of_product = QLineEdit()
        line_edit_quantity_of_product.setText(self.quantity)
        line_edit_quantity_of_product.setReadOnly(True)
        self.layout.addWidget(label_quantity)
        self.layout.addWidget(line_edit_quantity_of_product)        

        
        # Adicionando o QLabel e QLineEdit para Estoque Minimo
        label_minimum_stock = QLabel("Estoque Minimo:")
        self.line_edit_minimum_stock = QLineEdit()
        self.line_edit_minimum_stock.setText(self.minimum_stock)
        self.line_edit_minimum_stock.setValidator(validator_int) 
        

        self.layout.addWidget(label_minimum_stock)
        self.layout.addWidget(self.line_edit_minimum_stock)

        # Adicionando o QLabel e QLineEdit para Estoque Maximo
        label_maximus_stock = QLabel("Estoque Maximo:")
        self.line_edit_maximus_stock = QLineEdit()
        self.line_edit_maximus_stock.setText(self.maximum_stock)
        self.line_edit_maximus_stock.setValidator(validator_int) 
        self.layout.addWidget(label_maximus_stock)
        self.layout.addWidget(self.line_edit_maximus_stock)
        
        label_unit = QLabel("Unidade de Medida:")
        self.combo_box_unit = QComboBox()
        self.combo_box_unit.addItems([
            self.measurement_unit
            ])
        
        for unity in self.database_get.get_all_unity_of_mesurament_acronym():
            if unity[0] == self.measurement_unit:
                print(unity)
                pass
            else:
              self.combo_box_unit.addItems(unity) 
               
        self.layout.addWidget(label_unit)
        self.layout.addWidget(self.combo_box_unit)

        label_category = QLabel("Categoria:")
        self.combo_box_category = QComboBox()
        actual_product_category = self.categoria.upper()
        
        self.combo_box_category.addItems([
            actual_product_category
            ])
        for category in self.database_get.get_all_category():
            upper_category = category[0].upper()
            
            if upper_category == actual_product_category:
                pass
            else:
                self.combo_box_category.addItems(category)
                
        update_item_button = QPushButton()
        update_item_button.setText('Atualizar')
        update_item_button.clicked.connect(self.update_products_informations)

        self.layout.addWidget(label_category)
        self.layout.addWidget(self.combo_box_category)
        
        self.layout.addWidget(update_item_button)
        # Criando um widget para conter o layout vertical
        widget = QWidget()
        widget.setLayout(self.layout)

        # Adicionando o widget ao central widget da janela principal
        self.setCentralWidget(widget)


    def update_products_informations(self):
        selected_category_text_input = self.combo_box_category.currentText()
        mesuramente_unity_text_input = self.combo_box_unit.currentText()
        product_codebar_text_input = self.line_edit_code_bar.text()
        name_of_product_text_input = self.line_edit_product_name.text()
        cost_value_text_input = self.line_edit_cost_value.text()
        unitary_value_text_input = self.line_edit_unitary_value.text()
        minimum_stock_text_input = self.line_edit_minimum_stock.text()
        maximum_stock_text = self.line_edit_maximus_stock.text()
        
        product_code_changed = [False, None, None, None]
        product_name_changed = [False, None, None, None]
        product_cost_value_changed = [False, None, None, None]
        product_unitary_value_changed = [False, None, None, None]
        product_minimum_stock_changed = [False, None, None, None]
        product_maximum_stock_changed = [False, None, None, None]
        product_measurement_unit_changed = [False, None, None, None]
        product_category_changed = [False, None, None, None]
        
        category_text_input_upper = self.categoria.upper()
        #Verifica se foi alterado o CODIGO DE BARRAS do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.code_bar_of_product, product_codebar_text_input):
            #não foi alterado
            pass
        else:
            product_code_changed = [
                True,
                self.code_bar_of_product,
                product_codebar_text_input,
                'Codigo_do_produto'
                ]
            
            print('Do alter query CODIGO DE BARRAS')
            
        #Verifica se foi alterado o NOME DO PRODUTO comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.name_product_to_show, name_of_product_text_input):
            #não foi alterado
            pass
        else:
            product_name_changed = [
                True,
                self.name_product_to_show,
                name_of_product_text_input,
                'Nome'
                ]
            
            print('Do alter query NOME DO PRODUTO')  
            
        #Verifica se foi alterado o VALOR DE CUSTO comparando o nome inicial com o lineEdit 
        if self.verify_if_has_change_on_informations(self.cost_value, cost_value_text_input):
            #não foi alterado
            pass
        else:
            product_cost_value_changed = [
                True,
                self.cost_value,
                cost_value_text_input, 
                'Valor_de_custo'
                ]
            
            print('Do alter query VALOR DE CUSTO')  
            
        #Verifica se foi alterado o VALOR UNITARIO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.unitary_value, unitary_value_text_input):
            #não foi alterado
            pass
        else:
            product_unitary_value_changed = [
                True,
                self.unitary_value,
                unitary_value_text_input,
                'Valor_unitario'
                ]
            
            print('Do alter query VALOR UNITARIO')  
            
        #Verifica se foi alterado o ESTOQUE MINIMO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.minimum_stock , minimum_stock_text_input):
            #não foi alterado
            pass
        else:
            product_minimum_stock_changed = [
                True,
                self.minimum_stock,
                minimum_stock_text_input, 
                'Estoque_minimo'
                ]
            
            print('Do alter query ESTOQUE MINIMO') 
            
        #Verifica se foi alterado o ESTOQUE MAXIMO do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.maximum_stock ,maximum_stock_text ):
            #não foi alterado
            pass
        else:
            product_maximum_stock_changed = [
                True,
                self.maximum_stock,
                maximum_stock_text,
                'Estoque_maximo'
                ]
            
            print('Do alter query ESTOQUE MAXIMO')
        
        #Verifica se foi alterado A UNIDADE DE MEDIDA do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(self.measurement_unit ,mesuramente_unity_text_input ):
            #não foi alterado
            pass
        else:
            product_measurement_unit_changed = [
                True,
                self.measurement_unit,
                mesuramente_unity_text_input,
                'Unidade_de_medida'
                ]
            
            print('Do alter query UNIDADE DE MEDIDA')  
            
        #Verifica se foi alterado A CATEGORIA do produto comparando o nome inicial com o lineEdit
        if self.verify_if_has_change_on_informations(category_text_input_upper,selected_category_text_input ):
            #não foi alterado
            pass
        else:
            product_category_changed = [
                True,
                category_text_input_upper,
                selected_category_text_input, 
                'Categoria'
                ]
            print('Do alter query CATEGORIA')
            
        if self.verify_if_minimum_stock_is_less_than_maximum_stock(
            minimum_stock_text_input,
            maximum_stock_text):
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
                    product_category_changed):  
                    
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