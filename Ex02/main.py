import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from boateKiss import Ui_MainWindow  # Importa a interface gerada

class Boate(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelPergunta.setText(f"Qual a sua idade?")
        # Conectar o botão à função que realiza a soma
        self.ui.btnVerificar.clicked.connect(self.ehMaior)
    

    def ehMaior(self):
        try:
            idade = int(self.ui.inputDigite.text())

            if idade >= 18:
                self.ui.labelPergunta.setText('Pode entrar...')
            elif idade < 18:
                self.ui.labelPergunta.setText('Saia fora!')
            elif idade <= 10 or idade > 70:
                self.ui.labelPergunta.setText('Mentira...')
        except ValueError:
                self.ui.labelPergunta.setText('Use numeros...')






if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Boate()
    janela.show()
    sys.exit(app.exec_())
