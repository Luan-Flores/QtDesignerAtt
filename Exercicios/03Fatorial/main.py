import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from valdez import Ui_MainWindow  # Importa a interface gerada

class Fatorial(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.fatorialBtn.clicked.connect(self.calcular)

    def calcular(self):
        n=int(self.ui.lineEdit1.text())

        antecessor=n-1
        fatorial = n

        while antecessor > 0:
            fatorial *= antecessor 
            
            antecessor-=1
        
        # print(f"{n}! = {fatorial}")
        # Mostrar o resultado no rótulo
        try:
            self.ui.label_3.setText(f"Resultado: {fatorial}")
            
        except ValueError:
            self.ui.label_3.setText("Por favor, insira números válidos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Fatorial()
    janela.show()
    sys.exit(app.exec_())
