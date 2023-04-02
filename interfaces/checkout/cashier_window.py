import sys
import os
path = os.path.abspath('interfaces/checkout')
sys.path.append(path)
from product_informations_window import *
from cart_window import *
from PySide6 import  QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QWidget, QToolBar, QMessageBox
)
from PySide6.QtGui import QAction, QIcon
class CheckoutPage(QMainWindow):
    def __init__(self):
        super(CheckoutPage,self).__init__()
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Caixa')
        self.setMinimumSize(1024,720)
        self.widget = QWidget()
        self.layout_window = QVBoxLayout()
        #Add the menu options of the program
        self.config_the_toolbar()
        self.set_layout()
        self.products = []
    
    def config_the_toolbar(self):
        button_shop = QAction(QIcon(r'images/shopping-cart.png'),"Iniciar Venda" ,self)
        button_shop.triggered.connect(self.get_product_to_sell)
        tool = QToolBar()
        self.addToolBar(tool)
        tool.addAction(button_shop)
        
    def set_layout(self):
        self.widget.setLayout(self.layout_window)
        self.setCentralWidget(self.widget)
        
    def open_checkout(self, data):
        str_of_products = self.get_id_and_name_of_list(data)
        number_of_products_retorned = self.cont_products(data)
        if number_of_products_retorned >1:
            self.show_dialog(f'Foi retornado mais de um produto: \n {str_of_products}')
        else:
            have_item = False
            for item in self.products:
                if data[0][1] == item[1]:
                    print('ja tem')
                    have_item = True
                    break     
            if have_item == False:
                self.products.append(data[0])
                self.window_product.close()
                number_itens = self.get_number_of_products_to_show(self.products)
                self.show_products_list(self.products, number_itens)    
            else:
                self.show_dialog('O produto já exite na lista')

    def cont_products(self, list):
        number_of_products = 0
        for l in list:
            number_of_products += 1
        return number_of_products

    def get_id_and_name_of_list(self, list):
        string = ''
        for product in list:
            id_prod = str(product[0])
            name_prod = str(product[1])
            string = string+ '\nid: '+ id_prod+'\nnome: '+ name_prod +'\n'
        return string
               
    def get_product_to_sell(self):
        self.window_product = ProductsInfo(self)
        self.window_product.show()
        
    def get_number_of_products_to_show(self, list):
        n_of_itens = 0
        for n in list:
            n_of_itens += 1
        final_n = n_of_itens
        return final_n
        
    def show_products_list(self, list_of_itens, number_of_itens):
        cart_widget = CartWidget( list_of_itens,self)
        self.clear_layout(self.layout_window)
        self.set_layout()
        self.layout_window.addWidget(cart_widget)
        print(list_of_itens)
        
    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
    
    def show_dialog(self, text):
        QMessageBox.about(self, 'DIALOG', text)
   
if  __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = CheckoutPage()
    widget.show()
    sys.exit(app.exec())