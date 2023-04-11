import sys
from PySide6.QtWidgets import (
    QApplication,
   )

import os
path = os.path.abspath('database/database_manager')
sys.path.append(path)
from mesurement_window_base import MesuramentBase

class AddUnitWindow(MesuramentBase):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.button_add_unit_of_measurement.clicked.connect(self.add_unit)
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
                self.parent().reset_layout()
                self.close()
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
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AddUnitWindow()
    window.show()
    sys.exit(app.exec())
