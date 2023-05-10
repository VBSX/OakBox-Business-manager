import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
)
from PySide6.QtGui import QIcon
import os
path = os.path.abspath('./')
sys.path.append(path)
from database.database_manager.products_database import ProductsData
from interfaces.checkout.dialog_window_confirmation import *
from database.database_manager.add_product_database import AddProducts
from interfaces.checkout.dialog_window_confirmation import MyDialog

class WindowBaseClass(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.image_icon = ''
        
        self.database_insert = AddProducts()
        self.database_get = ProductsData()
        #config of the window
        
        self.setMinimumSize(950,320)
        self.setup_ui()

    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :30px;font-size:18px;margin-top:30px")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(64,64))
        
    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)
        
    def icon_set(self, icon):
        self.setWindowIcon(QtGui.QIcon(icon)) 
        
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
         
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = WindowBaseClass()
    widget.show()
    sys.exit(app.exec())