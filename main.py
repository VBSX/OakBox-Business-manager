from interfaces.login import*

app = QtWidgets.QApplication([])
login = LoginPage()
login.show()
sys.exit(app.exec())
