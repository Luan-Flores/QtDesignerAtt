import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from ifPrimo import Ui_MainWindow  # Importa a interface gerada

class ifPrimo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.confirmBtn.clicked.connect(self.isPrimo)

    def isPrimo(self):
        n = int(self.ui.inputLine.text()) 
        if n <= 1:
            self.ui.result.setText(f"NÃO")
            self.ui.result.setStyleSheet("color: red;border: 1px solid black; background-color: white")
        else:
            
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    self.ui.result.setText(f"NÃO")  
                    self.ui.result.setStyleSheet("color: red;border: 1px solid black; background-color: white")
                    break
            else:
                self.ui.result.setText(f"SIM")
                self.ui.result.setStyleSheet("color: green;border: 1px solid black; background-color: white") 



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = ifPrimo()
    janela.show()
    sys.exit(app.exec_())
