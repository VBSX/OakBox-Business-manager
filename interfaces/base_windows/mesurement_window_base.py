import sys
from PySide6.QtWidgets import (
    QVBoxLayout,
    QApplication,
    QWidget,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    )
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.base_windows.main_window_base import WindowBaseClass
class MesuramentBase(WindowBaseClass):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.image_icon = r'images/ruler.png'
         
    def setup_ui(self):
        self.setMinimumSize(350,100)
        self.icon_set(self.image_icon)
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
        
    def verify_fields(self):
        # Verifica se ambos os campos estão preenchidos
        name_written = bool(self.line_edit_unit_of_measurement.text())
        acronym_written = bool(self.line_edit_acronym.text())
        self.button_add_unit_of_measurement .setEnabled(name_written and acronym_written)

    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MesuramentBase()
    window.show()
    sys.exit(app.exec())
