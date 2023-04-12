import sys
from PySide6.QtWidgets import (
    QApplication,
   )
from PySide6 import QtCore
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.base_windows.mesurement_window_base  import MesuramentBase

class EditUnitWindow(MesuramentBase):
    def __init__(self,unit_name, unit_acronym,parent=None):
        super().__init__(parent)
        self.setWindowModality(QtCore.Qt.ApplicationModal)
        self.button_add_unit_of_measurement.setText('Atualizar Informações')
        self.actual_unit_name = unit_name
        self.actual_unit_acronym = unit_acronym
        unit_name_low = self.actual_unit_name.lower()
        unit_acronym_low = self.actual_unit_acronym.lower()
        self.line_edit_unit_of_measurement.setText(unit_name_low)
        self.line_edit_acronym.setText(unit_acronym_low)
        self.button_add_unit_of_measurement.clicked.connect(self.edit_unit_info)
        
    def edit_unit_info(self):
        # Obtém os valores dos campos
        name = self.line_edit_unit_of_measurement.text()
        name_upper = name.upper()
        acronym = self.line_edit_acronym.text()
        acronym_upper = acronym.upper()
        if name_upper == self.actual_unit_name and acronym_upper == self.actual_unit_acronym:
            self.show_dialog('Não ha alterações para aplicar')
        else:
            if self.verify_if_unit_exist_on_database(name,acronym):
                self.show_dialog('Esta unidade de medida já existe!')
            else:
                database_return = self.database_insert.update_unit_of_mesurament(
                    actual_name = self.actual_unit_name,
                    actual_acronym = self.actual_unit_acronym,
                    new_name = name_upper,
                    new_acronym = acronym_upper)
                
                if database_return:
                    self.show_dialog('Unidade de Medida editada com sucesso')
                    self.parent().reset_layout()
                    self.close()
                else:
                    self.show_dialog(f'erro:\n {database_return}')
        
    def verify_if_unit_exist_on_database(self,name,acronym):
        name_upper = name.upper()
        acronym_upper = acronym.upper()
        database_data_name_unit = self.database_get.get_especific_unity_by_name(name_upper)
        database_data_acronym_unit = self.database_get.get_especific_unity_by_acronym(acronym_upper)
        
        if database_data_name_unit and database_data_acronym_unit:
            return True
        else:
            return False
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditUnitWindow()
    window.show()
    sys.exit(app.exec())
