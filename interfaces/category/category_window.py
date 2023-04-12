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
from interfaces.category.add_new_category_window import CategoryAddWindow
from interfaces.category.edit_category_window import EditCategoryWindow
from database.database_manager.products_database import ProductsData
from database.database_manager.add_product_database import AddProducts
from interfaces.checkout.dialog_window_confirmation import *


class CategoryWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Categorias")
        self.database_get = ProductsData()
        self.database_insert = AddProducts()
        self.msg_dialog_item_deleted = 'Categoria deletada!'
        self.button_edit_item_text = "Editar a categoria"
        self.button_add_item_name_text = "Adicionar uma nova categoria"
        self.button_remove_item_text = "Deletar a categoria"
        self.setMinimumSize(300,400)
        self.config_the_toolbar() 
        self.setup_ui()
        
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
        self.all_itens = self.database_get.get_all_category()

        # Adiciona a primeira linha com os títulos
        item_titulos = QListWidgetItem(self.list_unidades)
        widget_titulos = QWidget()
        layout_titulos = QHBoxLayout()
        widget_titulos.setLayout(layout_titulos)

        label_nome_titulo = QLabel("Nome")

        layout_titulos.addWidget(label_nome_titulo)

        item_titulos.setSizeHint(widget_titulos.sizeHint())
        self.list_unidades.addItem(item_titulos)
        self.list_unidades.setItemWidget(item_titulos, widget_titulos)

        # Adiciona as unidades de medida na lista
        for name in self.all_itens:
            item = QListWidgetItem(self.list_unidades)
            widget = QWidget()
            layout = QHBoxLayout()
            widget.setLayout(layout)
            label_nome = QLabel(name[0])
            layout.addWidget(label_nome)

            item.setSizeHint(widget.sizeHint())
            self.list_unidades.addItem(item)
            self.list_unidades.setItemWidget(item, widget)

    def config_the_toolbar(self):
        self.button_edit_item = QAction(QIcon(r'images/pencil.png'),self.button_edit_item_text ,self)
        self.button_add_item_name = QAction(QIcon(r'images/plus.png'),self.button_add_item_name_text ,self)
        self.button_remove_item = QAction(QIcon(r'images/delete.png'),self.button_remove_item_text ,self)
        self.button_edit_item.triggered.connect(self.open_edit_item_window)
        self.button_add_item_name.triggered.connect(self.open_add_new_item_window)
        self.button_remove_item.triggered.connect(self.delete_item_selected)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(self.button_edit_item)
        tool.addAction(self.button_add_item_name)
        tool.addAction(self.button_remove_item)
        
    def delete_item_selected(self):
        row = self.list_unidades.currentRow()
        if row > 0: 
            self.do_delete(row)
            
    def do_delete(self,row):
        header = 1
        print(self.all_itens)
        selected_item_name = self.all_itens[row-header][0]
        
        if self.user_verify_continue_to_delete(selected_item_name): 
            
            database_return = self.database_insert.delete_some_category(
                selected_item_name)
            
            if database_return:
                self.show_dialog(self.msg_dialog_item_deleted)
                self.reset_layout()        
            else:
                self.show_dialog(f'erro:\n {database_return}')   

 
    def reset_layout(self):
        # Clear the central widget
        self.centralWidget().setParent(None)
        self.setup_ui()
                  
    def user_verify_continue_to_delete(self, name):
        msg_of_warning = f'Deseja continuar a deletar o item?\n\nNome: {name}\n'
        tela_de_confirmação = MyDialog(msg_of_warning,'Deletar Item',self)
        tela_de_confirmação.show()
        if tela_de_confirmação.exec() == QDialog.Accepted:
            return True
        else:
            return False
        
    def get_edit_item(self):
        row = self.list_unidades.currentRow()
        if row > 0: 
            self.open_edit_item_window(row)
            

    def open_edit_item_window(self, row):
        header = 1
        print(type(row))
        selected_item_name = self.all_itens[row-header]

        self.edit = EditCategoryWindow(selected_item_name[0], self)
        self.edit.show()
        
    def open_add_new_item_window(self):
        self.new_item_window = CategoryAddWindow(self)
        self.new_item_window.show()

    
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)

        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CategoryWindow()
    window.show()
    sys.exit(app.exec())
