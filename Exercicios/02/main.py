import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mediaTres import Ui_MainWindow  # Importa a interface gerada

class Media(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelResult.setText('Média: ')
        self.ui.okBtn.clicked.connect(self.calcular)
    
    def calcular(self):
        try:
                
            nMedia=[]
            counter=3

            n1=int(self.ui.lineEdit.text())
            n2=int(self.ui.lineEdit_2.text())
            n3=int(self.ui.lineEdit_3.text())

            nMedia.append(n1+n2+n3)
            resultado=sum(nMedia)/counter

            self.ui.labelResult.setText(f"Média aritmética: {resultado:.1f}")
        except ValueError:
            self.ui.labelResult.setText('Utilize apenas números!')
if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Media()
    janela.show()
    sys.exit(app.exec_())
