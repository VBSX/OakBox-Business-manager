import sys
from PySide6.QtWidgets import (
    QApplication,
)
import os
path = os.path.abspath('./')
sys.path.append(path)
from interfaces.base_windows.category_window_base import CategoryBase

class CategoryAddWindow(CategoryBase):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("Adicionar Nova Categoria")
        self.button_add_category.clicked.connect(self.add_category)

    def add_category(self):
        # Obtém os valores dos campos
        name = self.line_edit_category.text()
        name_upper = name.upper()

        if self.verify_if_category_exist_on_database(name_upper):
            self.show_dialog('Esta categoria já existe!')
        else:
            database_return = self.database_insert.add_new_category(name_upper)
            if database_return:
                self.show_dialog('Categoria adicionada com sucesso')
                self.parent().reset_layout()
                self.close()
            else:
                self.show_dialog(f'erro:\n {database_return}')
                
    def verify_if_category_exist_on_database(self,name):
        

        database_data_name_category = self.database_get.get_category_by_name(name)
        
        if database_data_name_category:
            return True
        else:
            return False
      
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CategoryAddWindow()
    window.show()
    sys.exit(app.exec())
