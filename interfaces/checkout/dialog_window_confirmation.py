from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton

class MyDialog(QDialog):
    def __init__(self, info,info_button, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tela Confirmação")
        self.info = info
        self.setModal(True)
        # Cria um QLabel para exibir as informações
        label = QLabel(self.info)
        # Cria dois QPushButton, um para Concluir e outro para Cancelar
        button_box = QHBoxLayout()
        conclui_button = QPushButton(f"{info_button}")
        conclui_button.clicked.connect(self.accept)  # Chama o método accept() quando o botão "Concluir" for pressionado
        cancela_button = QPushButton("Cancelar")
        cancela_button.clicked.connect(self.reject)  # Chama o método reject() quando o botão "Cancelar" for pressionado
        button_box.addWidget(conclui_button)
        button_box.addWidget(cancela_button)
        # Adiciona o QLabel e os botões ao layout vertical
        layout = QVBoxLayout()
        layout.addWidget(label)
        layout.addLayout(button_box)
        # Define o layout do diálogo
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    info = "Essas são as informações que serão exibidas no diálogo."
    dialog = MyDialog(info)
    if dialog.exec() == QDialog.Accepted:
        print("O botão 'Concluir' foi pressionado.")
    else:
        print("O botão 'Cancelar' foi pressionado.")
    app.exit()