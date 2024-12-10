import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from tabuada import Ui_MainWindow  # Importa a interface gerada

class Tabuada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resultado.setText('Resultado: ')
        self.ui.botao.clicked.connect(self.calcular)
    
    def calcular(self):
        try:
            result=[]                
            nTab=int(input('insert a number: '))
            for i in range(11):
                dor = (f'{nTab} x {i} = {nTab*i}')
                result.append(dor)
            self.ui.resultado.setText(dor)

        except ValueError:
            self.ui.resultado.setText('Utilize apenas números!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Tabuada()
    janela.show()
    sys.exit(app.exec_())
