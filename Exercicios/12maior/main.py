

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from maior import Ui_MainWindow  # Importa a interface gerada

class Maiorde3(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.botao.clicked.connect(self.calcular)

    def calcular(self):
        try:
            numero1 = float(self.ui.input.text())
            numero2 = float(self.ui.input_2.text())
            numero3 = float(self.ui.input_3.text())

            maior = max(numero1, numero2, numero3)

            self.ui.resultado.setText(f"O maior número é: {maior}")
            
        except ValueError:
            self.ui.resultado.setText("Por favor, insira números válidos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Maiorde3()
    janela.show()
    sys.exit(app.exec_())
