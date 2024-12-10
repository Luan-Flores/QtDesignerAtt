import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from quadrado import Ui_MainWindow

class Quadrado(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resultado.setText('Resultado: ')
        self.ui.botao.clicked.connect(self.calcular)
    
    def calcular(self):
        try:
            n = int(self.ui.input.text())
            resultado = n * n
            self.ui.resultado.setText(f"Resultado: {resultado}")
        except ValueError:
            self.ui.resultado.setText('Utilize apenas números!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Quadrado()
    janela.show()
    sys.exit(app.exec_())
