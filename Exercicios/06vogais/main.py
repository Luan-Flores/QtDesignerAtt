import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from vogal import Ui_MainWindow  # Importa a interface gerada

class Vogalzada(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelResult.setText('Vogais: ')
        self.ui.pushButton.clicked.connect(self.contar)
    
    def contar(self):
        try:
            word=str(self.ui.input.text())
            count=0
            vogais={'a','e','i','o','u'}
            for letra in word:
                if letra.lower() in vogais:
                    count+=1
                    print(count)
                print(count)
            self.ui.labelResult.setText(f'Vogais: {count}')

        except ValueError:
            print('Apenas letras')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Vogalzada()
    janela.show()
    sys.exit(app.exec_())