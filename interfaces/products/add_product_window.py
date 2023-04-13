from PySide6.QtWidgets import (QPushButton,
QComboBox, QWidget, QLineEdit,QApplication,QLabel,
QMainWindow, QMessageBox,QHBoxLayout,QVBoxLayout )
from PySide6.QtGui import Qt,QDoubleValidator,QIntValidator, QIcon
import sys
import os
path = os.path.abspath('./')
sys.path.append(path)
from database.database_manager.add_product_database import AddProducts
from database.database_manager.products_database import ProductsData

class WindowProductAdd(QMainWindow):
    def __init__(self, parent = None):
        super(WindowProductAdd, self).__init__(parent = parent)
        self.setWindowTitle('Adicionar Produto')
        self.setMinimumWidth(600)
        self.add_icon = r'images/plus.png'
        self.database_handle_add = AddProducts()
        self.database_handle_consult = ProductsData()
        self.setup_ui()
        
    def setup_ui(self):
        self.layout = QVBoxLayout()
        self.message_init = QLabel()
        self.message_init.setText('Coloque as informações do novo produto: ')
        self.add = QPushButton("Adicionar novo produto", clicked=self.send_new_product)
        self.add.setIcon(QIcon(self.add_icon))
        self.layout.addWidget(self.message_init)
        
        layout_codigo_barras = QHBoxLayout()
        layout_codigo_barras.setSpacing(10)
        layout_codigo_barras.setAlignment(Qt.AlignLeft)  
        self.codigo_produto_label = QLabel("Codigo de barras produto:")
        self.codigo_produto_edit = QLineEdit()
        self.codigo_produto_edit.returnPressed.connect(self.add.click)
        layout_codigo_barras.addWidget(self.codigo_produto_label, 0, Qt.AlignLeft)
        layout_codigo_barras.addWidget(self.codigo_produto_edit, 0, Qt.AlignLeft)
        self.layout.addLayout(layout_codigo_barras)
        
        layout_layout_nome_produto = QHBoxLayout()
        layout_layout_nome_produto.setSpacing(10)
        layout_layout_nome_produto.setAlignment(Qt.AlignLeft)
        self.produto_label = QLabel("Nome do produto:")
        self.produto_edit = QLineEdit()
        self.produto_edit.returnPressed.connect(self.add.click)
        layout_layout_nome_produto.addWidget(self.produto_label, 0, Qt.AlignLeft)
        layout_layout_nome_produto.addWidget(self.produto_edit, 0, Qt.AlignLeft) 
        self.layout.addLayout(layout_layout_nome_produto)
        # Configurando os input do valor de custo  
        layout_valor_custo = QHBoxLayout()
        layout_valor_custo.setSpacing(10)
        layout_valor_custo.setAlignment(Qt.AlignLeft)
        label_valor_custo = QLabel("Valor de Custo:")
        self.line_edit_valor_custo = QLineEdit()
        # Criar um QLabel para o sulfixo
        label_valor_custo_suffix = QLabel("R$")
        # Criar um QDoubleValidator para validar o input do usuário
        validator_double = QDoubleValidator()    
        validator_double.setBottom(1)  # Define o limite para que não seja permitido negativos
        validator_double.setDecimals(2)
        validator_double.setNotation(QDoubleValidator.StandardNotation)

        #Validador para numeros inteiros e positivos
        validator_int = QIntValidator()
        validator_int.setBottom(1)
        
        # Adicionar o validator no QLineEdit
        self.line_edit_valor_custo.setValidator(validator_double)
        self.line_edit_valor_custo.setFixedWidth(100)
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_valor_custo.addWidget(label_valor_custo, 0, Qt.AlignLeft)
        layout_valor_custo.addWidget(label_valor_custo_suffix, 0, Qt.AlignLeft)
        layout_valor_custo.addWidget(self.line_edit_valor_custo, 0, Qt.AlignLeft)
        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_valor_custo)
        
        #Configs do input do valor unitario
        self.valor_unitario_label = QLabel("Valor unitario: ")
        self.valor_unitario_edit  = QLineEdit()
        # Criar um QLabel para o sulfixo
        label_valor_unitario_suffix = QLabel("R$")
        
        # Adicionar o validator no QLineEdit
        self.valor_unitario_edit.setValidator(validator_double)
        self.valor_unitario_edit.setFixedWidth(100)
        # Adicionar o QLineEdit e o QLabel no QHBoxLayout
        layout_valor_custo.addWidget(self.valor_unitario_label, 0, Qt.AlignLeft)
        layout_valor_custo.addWidget(label_valor_unitario_suffix, 0, Qt.AlignLeft)
        layout_valor_custo.addWidget(self.valor_unitario_edit, 0, Qt.AlignLeft)
        # Adicionar o QHBoxLayout na grid layout
        self.layout.addLayout(layout_valor_custo)
        
        
        layout_quantidade = QHBoxLayout()
        layout_quantidade.setSpacing(10)
        layout_quantidade.setAlignment(Qt.AlignLeft)
        
        self.quantidade_label = QLabel("Quantidade:")
        self.quantidade_edit = QLineEdit()
        self.quantidade_edit.setText('0')
        self.quantidade_edit.setFixedWidth(15)
        self.quantidade_edit.setReadOnly(True)
        layout_quantidade.addWidget(self.quantidade_label, 0, Qt.AlignLeft)
        layout_quantidade.addWidget(self.quantidade_edit, 0, Qt.AlignLeft)
        self.layout.addLayout(layout_quantidade)
        
        layout_estoque = QHBoxLayout()
        layout_estoque.setSpacing(10)
        layout_estoque.setAlignment(Qt.AlignLeft)
        
        self.estoque_minimo_label = QLabel("Estoque mínimo:")
        self.estoque_minimo_edit = QLineEdit()
        self.estoque_minimo_edit.returnPressed.connect(self.add.click)
        self.estoque_minimo_edit.setValidator(validator_int) 
        layout_estoque.addWidget(self.estoque_minimo_label, 0, Qt.AlignLeft)
        layout_estoque.addWidget(self.estoque_minimo_edit, 0, Qt.AlignLeft)

        
        self.estoque_maximo_label = QLabel("Estoque máximo:")
        self.estoque_maximo_edit = QLineEdit()
        self.estoque_maximo_edit.setValidator(validator_int) 
        self.estoque_maximo_edit.returnPressed.connect(self.add.click)
        layout_estoque.addWidget(self.estoque_maximo_label, 0, Qt.AlignLeft)
        layout_estoque.addWidget(self.estoque_maximo_edit, 0, Qt.AlignLeft)
        self.layout.addLayout(layout_estoque)
        
        
        layout_unidade_medida = QHBoxLayout()
        layout_unidade_medida.setSpacing(10)
        layout_unidade_medida.setAlignment(Qt.AlignLeft)
        self.unidade_medida_label = QLabel("Unidade medida:")
        self.combo_box_unidade = QComboBox()
        for unity_mesurement in self.database_handle_consult.get_all_unity_of_mesurament_acronym():
            self.combo_box_unidade.addItems(
                unity_mesurement
                )
        layout_unidade_medida.addWidget(self.unidade_medida_label, 0, Qt.AlignLeft)
        layout_unidade_medida.addWidget(self.combo_box_unidade, 0, Qt.AlignLeft)
        self.layout.addLayout(layout_unidade_medida)


        layout_category = QHBoxLayout()
        layout_category.setSpacing(10)
        layout_category.setAlignment(Qt.AlignLeft)
        self.categoria_label = QLabel("Categoria:")
        self.combo_categoria = QComboBox()
        for category in self.database_handle_consult.get_all_category():
            self.combo_categoria.addItems(
                category
                )
        layout_category.addWidget(self.categoria_label, 0, Qt.AlignLeft)
        layout_category.addWidget(self.combo_categoria, 0, Qt.AlignLeft)
        self.layout.addLayout(layout_category) 
        
        self.layout.addWidget(self.add)
        # Criando um widget para conter o layout vertical
        widget = QWidget()
        widget.setLayout(self.layout)
        # Adicionando o widget ao central widget da janela principal
        self.setCentralWidget(widget)
        
    def send_new_product(self):
        nome = self.produto_edit.text()
        nome_lower = nome.lower()
        quantidade = '0'
        codigo_de_barras = self.codigo_produto_edit.text()
        valor_custo = self.line_edit_valor_custo.text()
        valor_por_unidade = self.valor_unitario_edit.text()
        estoque_minimo = self.estoque_minimo_edit.text()
        estoque_maximo = self.estoque_maximo_edit.text()
        unidade_de_medida = self.combo_box_unidade.currentText()
        categoria = self.combo_categoria.currentText()
        
        if self.verify_in_field_is_not_null(
            nome,
            quantidade,
            codigo_de_barras,
            valor_custo,
            valor_por_unidade,
            estoque_minimo,
            estoque_maximo,
            unidade_de_medida,
            categoria):

            if self.verify_if_product_exist_on_database(nome_lower) == False:
                if self.verify_if_minimum_stock_is_less_than_maximum_stock(estoque_minimo,estoque_maximo):
                    database_return = self.database_handle_add.add_on_database_new_product(
                        codigo_de_barras,
                        nome,
                        valor_custo,
                        valor_por_unidade,
                        quantidade,       
                        estoque_minimo,
                        estoque_maximo,
                        unidade_de_medida,
                        categoria)
                    
                    if database_return  == True: 
                        self.show_dialog('Produto Adicionado com sucesso!')
                        self.reset_layout()
                        self.close()
                        self.parent().reset_layout()
                    else: 
                        self.show_dialog('erro ao adicionar')     
                else:
                    self.show_dialog('O estoque minimo tem que ser menor do que o estoque maximo!')    
            else:
                self.show_dialog('O produto ja existe!')

    def verify_in_field_is_not_null(
            self,   
            nome,
            quantidade,
            codigo_de_barras,
            valor_custo,
            valor_por_unidade,
            estoque_minimo,
            estoque_maximo,
            unidade_de_medida,
            categoria):

        if (nome 
            and quantidade
            and codigo_de_barras 
            and valor_custo
            and valor_por_unidade
            and estoque_minimo
            and estoque_maximo
            and unidade_de_medida
            and categoria):
            return True
        else:
            self.show_dialog('Prencha os campos antes de continuar')
        
    def verify_if_product_exist_on_database(self,nome):

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
        
    def reset_layout(self):
        # Clear the central widget
        self.centralWidget().setParent(None)
        self.setup_ui()
                
    def verify_if_minimum_stock_is_less_than_maximum_stock(self,estoque_minimo,estoque_maximo):
        if int(estoque_minimo) < int(estoque_maximo):
            return True
          
if __name__ == "__main__":
    app = QApplication([])
    widget = WindowProductAdd()
    widget.show()
    sys.exit(app.exec())