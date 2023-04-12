import sys
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QWidget,
    QMainWindow,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QToolBar,
    QHBoxLayout,
    QMessageBox,
    QDialog)
from PySide6.QtGui import QAction,QIcon

import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.mesurament_unity.add_mesurament_unit_window import AddUnitWindow
from interfaces.mesurament_unity.edit_mesurement_unit import EditUnitWindow
from database.database_manager.products_database import ProductsData
from database.database_manager.add_product_database import AddProducts
from interfaces.checkout.dialog_window_confirmation import MyDialog

class WindowUnit(QMainWindow):
    def __init__(self, parent= None):
        super().__init__(parent)
        self.setWindowTitle("Unidades de Medida")
        self.database_get = ProductsData()
        self.database_insert = AddProducts()
        self.setMinimumSize(300,400)
        self.config_the_toolbar()
        self.setup_ui()
        self.setWindowIcon(QIcon(r'images/ruler.png'))
        self.add_unit = AddUnitWindow(self)

    def setup_ui(self):
        # Criação dos widgets
        self.list_unidades = QListWidget()

        # Configuração dos layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout_principal = QVBoxLayout()
        central_widget.setLayout(layout_principal)

        layout_principal.addWidget(self.list_unidades)
        # Preenche a lista de unidades de medida
        self.preencher_lista()
        
    def preencher_lista(self):
        self.all_measurement_unity = self.database_get.get_all_unity_of_mesurament_info()

        # Adiciona a primeira linha com os títulos
        item_titulos = QListWidgetItem(self.list_unidades)
        widget_titulos = QWidget()
        layout_titulos = QHBoxLayout()
        widget_titulos.setLayout(layout_titulos)

        label_nome_titulo = QLabel("Nome")
        label_sigla_titulo = QLabel("Sigla")

        layout_titulos.addWidget(label_nome_titulo)
        layout_titulos.addWidget(label_sigla_titulo)

        item_titulos.setSizeHint(widget_titulos.sizeHint())
        self.list_unidades.addItem(item_titulos)
        self.list_unidades.setItemWidget(item_titulos, widget_titulos)

        # Adiciona as unidades de medida na lista
        for name, sigla in self.all_measurement_unity:
            item = QListWidgetItem(self.list_unidades)
            widget = QWidget()
            layout = QHBoxLayout()
            widget.setLayout(layout)

            label_nome = QLabel(name)
            label_sigla = QLabel(sigla)

            layout.addWidget(label_nome)
            layout.addWidget(label_sigla)

            item.setSizeHint(widget.sizeHint())
            self.list_unidades.addItem(item)
            self.list_unidades.setItemWidget(item, widget)
            
    def config_the_toolbar(self):
        button_edit_measurement_unity = QAction(QIcon(r'images/pencil.png'),"Editar Unidade de medida" ,self)
        button_edit_measurement_unity.triggered.connect(self.open_edit_mesurement_unit_window)
        button_add_measurement_unity = QAction(QIcon(r'images/plus.png'),"Adicionar Unidade de medida" ,self)
        button_add_measurement_unity.triggered.connect(self.add_new_category_window)
        button_remove_measurement_unity = QAction(QIcon(r'images/delete.png'),"Remover Unidade de medida" ,self)
        button_remove_measurement_unity.triggered.connect(self.delete_mesurement_unit)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_edit_measurement_unity)
        tool.addAction(button_add_measurement_unity)
        tool.addAction(button_remove_measurement_unity)

    def add_new_category_window(self):
        self.add_unit.show()
        
    def reset_layout(self):
        # Clear the central widget
        self.centralWidget().setParent(None)
        self.setup_ui()
        
    def open_edit_mesurement_unit_window(self):
        row = self.list_unidades.currentRow()
        header = 1
        if row > 0: 
            selected_item_name = self.all_measurement_unity[row-header][0]
            selected_item_acronym = self.all_measurement_unity[row-header][1]
            self.edit = EditUnitWindow(selected_item_name,selected_item_acronym, self)
            self.edit.show()
    
    def delete_mesurement_unit(self):
        row = self.list_unidades.currentRow()
        header = 1
        if row > 0: 
            selected_item_name = self.all_measurement_unity[row-header][0]
            selected_item_acronym = self.all_measurement_unity[row-header][1]
            if self.user_verify_continue_to_delete(selected_item_name, selected_item_acronym): 
                database_return = self.database_insert.delete_some_unit_of_mesurament(
                    selected_item_name,
                    selected_item_acronym)
                
                if database_return:
                    self.show_dialog('Unidade de Medida deletada com sucesso!')
                    self.reset_layout()        
                else:
                    self.show_dialog(f'erro:\n {database_return}')
                      
    def user_verify_continue_to_delete(self, name, acronym):
        msg_of_warning = f'Deseja continuar a deletar o item?\n\nNome: {name}\nSigla: {acronym}\n'
        tela_de_confirmação = MyDialog(msg_of_warning,'Deletar Item',self)
        tela_de_confirmação.show()
        if tela_de_confirmação.exec() == QDialog.Accepted:
            return True
        else:
            return False
        
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowUnit()
    window.show()
    sys.exit(app.exec())
