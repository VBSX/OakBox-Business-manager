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
    QHBoxLayout)
from PySide6.QtGui import QAction,QIcon
from add_mesurament_unit_window import AddCategoryWindow
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import ProductsData


class WindowUnit(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Unidades de Medida")
        self.database_get = ProductsData()
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
        # button_edit_measurement_unity.triggered.connect(self.product_edit_window)
        button_add_measurement_unity = QAction(QIcon(r'images/plus.png'),"Adicionar Unidade de medida" ,self)
        button_add_measurement_unity.triggered.connect(self.add_new_category_window)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_edit_measurement_unity)
        tool.addAction(button_add_measurement_unity)

    def add_new_category_window(self):
        self.category_window = AddCategoryWindow(self)
        self.category_window.show()
    
    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WindowUnit()
    window.show()
    sys.exit(app.exec())
