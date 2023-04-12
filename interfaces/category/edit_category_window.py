import sys
from PySide6.QtWidgets import (
    QApplication,
   )
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.base_windows.category_window_base  import CategoryBase

class EditCategoryWindow(CategoryBase):
    def __init__(self,category_name,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Editar Categoria")
        self.button_add_category.setText('Atualizar Informações da categoria')
        self.actual_category_name = category_name
        category_name_low = self.actual_category_name.lower()
        self.line_edit_category.setText(category_name_low)
        self.button_add_category.clicked.connect(self.edit_unit_info)
        
    def edit_unit_info(self):
        # Obtém os valores dos campos
        name = self.line_edit_category.text()
        name_upper = name.upper()
        if name_upper == self.actual_category_name:
            self.show_dialog('Não ha alterações para aplicar')
        else:
            if self.verify_if_category_exist_on_database(name):
                self.show_dialog('Esta Categoria já existe!')
            else:
                database_return = self.database_insert.update_category_item(
                    actual_name = self.actual_category_name,
                    new_name = name_upper,
                    )
                
                if database_return:
                    self.show_dialog('Categoria editada com sucesso')
                    self.parent().reset_layout()
                    self.close()
                else:
                    self.show_dialog(f'erro:\n {database_return}')
        
    def verify_if_category_exist_on_database(self,name):
        name_upper = name.upper()
        database_data_name_unit = self.database_get.get_category_by_name(name_upper)
        if database_data_name_unit:
            return True
        else:
            return False
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EditCategoryWindow()
    window.show()
    sys.exit(app.exec())
