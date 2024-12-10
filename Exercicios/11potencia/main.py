import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from potencia import Ui_MainWindow  # Importa a interface gerada

class Potencia(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.botao.clicked.connect(self.calcular)

    def calcular(self):
        try:
            base = int(self.ui.input.text())
            expoente=float(self.ui.input_2.text())
            result=base**expoente
            texto = (f"{base}^{expoente} = {result}")
            self.ui.resultado.setText(f"{texto}")
            
        except ValueError:
            self.ui.resultado.setText("Por favor, insira números válidos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Potencia()
    janela.show()
    sys.exit(app.exec_())
