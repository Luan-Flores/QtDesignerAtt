import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from edilson import Ui_MainWindow

class Edilson(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.resultado.setText('Resultado: ')
        self.ui.botao.clicked.connect(self.calcular)
    
    def calcular(self):
        try:
            counter=0
            soma=0
            n = int(self.ui.input.text())
            
            while counter < n:
                self.ui.input.setText('')
                nmr=int(self.ui.input.text())
                soma+=nmr
                counter+=1

            self.ui.resultado.setText(f'Media: {soma}')
        
        except ValueError:
            self.ui.resultado.setText('Utilize apenas números!')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Edilson()
    janela.show()
    sys.exit(app.exec_())
