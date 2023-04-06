import sys
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QWidget,
    QGridLayout,
    QMainWindow,
    QLabel,
    QLineEdit,
    QPushButton,
    QMessageBox)
from PySide6.QtGui import QIcon
import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from products_database import ProductsData
from add_product_database import AddProducts

class AddCategoryWindow(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Unidade de Medida")
        self.setMinimumSize(350,100)
        self.setWindowIcon(QIcon())
        self.database_get = ProductsData()
        self.database_insert = AddProducts()
        self.setup_ui()
         
    def setup_ui(self):
        # Criação dos widgets
        self.label_name_unit_of_measurement  = QLabel("Nome da Unidade de Medida:")
        self.line_edit_unit_of_measurement = QLineEdit()
        self.label_acronym_unit_of_measurement  = QLabel("Sigla da Unidade de Medida:")
        self.line_edit_acronym = QLineEdit()
        self.line_edit_acronym.setMaxLength(3)
        self.button_add_unit_of_measurement  = QPushButton("Adicionar")

        # Configuração dos layouts
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        field_layout = QGridLayout()
        main_layout.addLayout(field_layout)

        field_layout.addWidget(self.label_name_unit_of_measurement , 0, 0)
        field_layout.addWidget(self.line_edit_unit_of_measurement, 0, 1)
        field_layout.addWidget(self.label_acronym_unit_of_measurement , 1, 0)
        field_layout.addWidget(self.line_edit_acronym, 1, 1)
        field_layout.addWidget(self.button_add_unit_of_measurement , 2, 1)

        # Conexão do botão com o método de adicionar unidade de medida
        self.button_add_unit_of_measurement .setEnabled(False)  # Desabilita o botão no início
        self.line_edit_unit_of_measurement.textChanged.connect(self.verify_fields)
        self.line_edit_acronym.textChanged.connect(self.verify_fields)
        self.button_add_unit_of_measurement .clicked.connect(self.add_unit)

    def verify_fields(self):
        # Verifica se ambos os campos estão preenchidos
        name_written = bool(self.line_edit_unit_of_measurement.text())
        acronym_written = bool(self.line_edit_acronym.text())
        self.button_add_unit_of_measurement .setEnabled(name_written and acronym_written)

    def add_unit(self):
        # Obtém os valores dos campos
        name = self.line_edit_unit_of_measurement.text()
        acronym = self.line_edit_acronym.text()
        if self.verify_if_unit_exist_on_database(name,acronym):
            self.show_dialog('Esta unidade de medida já existe!')
        else:
            database_return = self.database_insert.add_new_unit_of_mesurament(name,acronym)
            if database_return:
                self.show_dialog('Unidade de Medida adicionada com sucesso')
            else:
                self.show_dialog(f'erro:\n {database_return}')
        
    def verify_if_unit_exist_on_database(self,name,acronym):
        name_upper = name.upper()
        acronym_upper = acronym.upper()
        database_data_name_unit = self.database_get.get_especific_unity_by_name(name_upper)
        database_data_acronym_unit = self.database_get.get_especific_unity_by_acronym(acronym_upper)
        
        if database_data_name_unit or database_data_acronym_unit:
            return True
        else:
            return False
        
        
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddCategoryWindow()
    window.show()
    sys.exit(app.exec())
