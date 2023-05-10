import sys
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QWidget,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QToolBar,
    QHBoxLayout,
    )
from PySide6.QtGui import QAction,QPalette, QColor, Qt, QIcon
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.category.add_new_category_window import CategoryAddWindow
from interfaces.category.edit_category_window import EditCategoryWindow
from interfaces.base_windows.main_window_base import WindowBaseClass

class CategoryWindow(WindowBaseClass):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_icon = r'images/category.png'
        self.msg_dialog_item_deleted = 'Categoria deletada!'
        self.button_edit_item_text = "Editar a categoria"
        self.button_add_item_name_text = "Adicionar uma nova categoria"
        self.button_remove_item_text = "Deletar a categoria"
        self.config_the_toolbar() 

    def setup_ui(self):
        # window config
        self.setWindowTitle("Categorias")
        self.setMinimumSize(300,400)
        self.icon_set(self.image_icon)
        # Criação dos widgets
        self.list_unidades = QListWidget()
        self.list_unidades.itemSelectionChanged.connect(self.on_item_selection_changed)
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
        
    def on_item_selection_changed(self):
        # Obter a lista de itens selecionados
        selected_items = self.list_unidades.selectedItems()

        # Definir a cor do texto dos itens selecionados como vermelho
        palette = QPalette()
        color = QColor(Qt.blue)
        palette.setColor(QPalette.Text, color)

        # Percorrer os itens selecionados e definir a paleta de cor
        for item in selected_items:
            item.setForeground(color)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CategoryWindow()
    window.show()
    sys.exit(app.exec())
