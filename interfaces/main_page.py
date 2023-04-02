import sys
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import (
    QMainWindow, 
    QHBoxLayout,QWidget, QPushButton, QDockWidget, QTextEdit
)
from PySide6.QtGui import QAction, QIcon, Qt, QDesktopServices, QPalette, QColor
from PySide6.QtCore import QUrl

import os
from login import *
path = os.path.abspath('interfaces/products')
sys.path.append(path)
from products.products_window import *
sys.path.append('interface/stock')
sys.path.append(path)
from stock.window_stock import *
from checkout.cashier_window import CheckoutPage

class MainPage(QMainWindow):
    def __init__(self):
        super(MainPage,self).__init__()
        self.image_test = r'images/filter.png'
        filter_icon_path = self.image_test
        #config of the window
        self.setWindowIcon(QtGui.QIcon(filter_icon_path))
        self.setWindowTitle('Main Page')
        self.setMinimumSize(1024,720)
        #Add the menu options of the program
        
        self.config_the_menubar()
        
        # Set up the main window and sidebar
        self.create_main_layout()
        self.set_dark_mode('enable')
        
    def create_main_layout(self):
        # Create a QWidget for the main content
        
        widget = QWidget()
        layout = QHBoxLayout()
        self.button_products = QPushButton("Produtos", clicked=self.open_products_window)
        self.button_estoque = QPushButton("Estoque", clicked=self.abrir_janela_estoque)
        self.button_caixa = QPushButton("Caixa", clicked=self.abrir_caixa)
        
        self.set_icons_and_resize_and_alter_font(self.button_caixa, self.image_test)
        self.set_icons_and_resize_and_alter_font(self.button_estoque, self.image_test)
        self.set_icons_and_resize_and_alter_font(self.button_products, self.image_test)
        layout.addWidget(self.button_estoque)
        layout.addWidget(self.button_products)
        layout.addWidget(self.button_caixa)
        
        widget.setLayout(layout)

        # Set the main window widget
        main_layout = QVBoxLayout()
        main_layout.addWidget(
            widget)
        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
        self.create_sidebar()

    def create_sidebar(self):
        # Create a QDockWidget for the sidebar
        self.sidebar = QDockWidget("Sidebar", self)
        self.sidebar.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)
        
        # Create a QTextEdit widget to hold the contents of the sidebar
        self.sidebar_contents = QTextEdit()
        self.sidebar_contents.setReadOnly(True)
        self.sidebar.setWidget(self.sidebar_contents)
        self.sidebar.setFixedWidth(200)
        
        # Add a button widget to the sidebar to open the GitHub link
        self.github_button = QPushButton("GitHub")
        self.github_button.clicked.connect(lambda: QDesktopServices.openUrl(QUrl("https://github.com/vbsx")))
        
        self.reset_sidebar_button = QPushButton("Voltar Ao Menu")
        self.reset_sidebar_button.clicked.connect(self.reset_layout)
        
        # Add the buttons to the sidebar layout
        self.sidebar_contents_layout = QVBoxLayout()
        self.sidebar_contents_layout.addWidget(self.github_button)
        self.sidebar_contents_layout.addWidget(self.reset_sidebar_button)
        self.sidebar_contents_layout.addStretch()
        
        # Create a container widget to hold the sidebar layout
        self.sidebar_contents_container = QWidget()
        self.sidebar_contents_container.setLayout(self.sidebar_contents_layout)
        self.sidebar.setWidget(self.sidebar_contents_container)
        
        # Add the sidebar to the left dock widget area
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)
            # Add the sidebar to the left dock widget area and set it as fixed
        self.addDockWidget(Qt.LeftDockWidgetArea, self.sidebar)
        self.sidebar.setFixedHeight(self.height())
        self.sidebar.setFeatures(QDockWidget.DockWidgetMovable | QDockWidget.DockWidgetFloatable | QDockWidget.NoDockWidgetFeatures)


    def reset_layout(self):
        # Remove all widgets from the sidebar layout
        while self.sidebar_contents_layout.count() > 0:
            item = self.sidebar_contents_layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.setParent(None)
        # Remove the sidebar from the dock widget area
        self.removeDockWidget(self.sidebar)
        self.sidebar.setParent(None)
        
        # Remove the central widget
        self.centralWidget().setParent(None)
    
    # Recreate the layout
        self.create_main_layout()
        
    def set_icons_and_resize_and_alter_font(self, item, icon):
        item.setStyleSheet("padding :30px;font-size:18px;margin-top:30px")
        item.setIcon(QIcon(icon))
        item.setIconSize(QtCore.QSize(64,64))
    
    def logoff(self):
        self.close()
        self.login = LoginPage()
        self.login.show()

    def show_dialog(self, text):
        QtWidgets.QMessageBox.about(self, 'DIALOG', text)

    def config_the_menubar(self):   
        button_action_logoff = QAction("logoff", self)
        button_action_logoff.triggered.connect(self.logoff)
        bar=self.menuBar()
        file=bar.addMenu('File')
        file.addAction('self.teste')
        log = bar.addMenu('Usuário')
        log.addAction(button_action_logoff)
       
    def open_products_window(self):
        self.w_product = ProductsPage()
        self.setCentralWidget(self.w_product)
        
        
    def abrir_janela_estoque(self):
        self.janela_estoque = StockPage()
        self.setCentralWidget(self.janela_estoque)
        
    def abrir_caixa(self):
        self.janela_caixa = CheckoutPage()
        self.setCentralWidget(self.janela_caixa)
        
    def set_dark_mode(self, enabled):
        if enabled:
            qApp.setStyle("Fusion")
            dark_palette = QPalette()
            dark_palette.setColor(QPalette.Window, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.WindowText, Qt.white)
            dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
            dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
            dark_palette.setColor(QPalette.ToolTipText, Qt.white)
            dark_palette.setColor(QPalette.Text, Qt.white)
            dark_palette.setColor(QPalette.Button, QColor(53, 53, 53))
            dark_palette.setColor(QPalette.ButtonText, Qt.white)
            dark_palette.setColor(QPalette.BrightText, Qt.red)
            dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
            dark_palette.setColor(QPalette.HighlightedText, Qt.black)
            dark_palette.setColor(QPalette.PlaceholderText, Qt.white)
            qApp.setPalette(dark_palette)
            
        else:
            qApp.setStyle("Fusion")
            qApp.setPalette(QApplication.style().standardPalette())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    
    widget = MainPage()
    
    widget.show()
    sys.exit(app.exec())