import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from SalaDeAula import Ui_MainWindow  # Importa a interface gerada

class Sala(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.labelResult.setText(f"90 ou + : Excelente\n70 ou + : Bom\n50 ou + : Regular\nMenor que 50: Insuficiente\n")
        # Conectar o botão à função que realiza a soma
        self.ui.verifyBtn.clicked.connect(self.CalcNota)
        self.teste=self.ui.labelResult

    def CalcNota(self):
        self.estilo=self.ui.labelResult.setStyleSheet("color: white; background-color: transparent;font: 22pt 'Snap ITC';")
        self.invalidMsg=self.ui.labelResult.setText("Nota inválida")
        try:
            nota = float(self.ui.inputLabel.text()) 
            if nota > 100 or nota < 0:
                self.invalidMsg
                self.estilo
                
                
            elif nota >= 90:
                self.ui.labelResult.setText("Excelente!")
                self.estilo
                
            elif nota >= 70:
                self.ui.labelResult.setText('Bom!')
                self.estilo
            elif nota >= 50:
                self.ui.labelResult.setText('Regular...')
                self.estilo
            else:
                self.ui.labelResult.setText('Insuficiente!')
                self.estilo

        except ValueError:
            self.invalidMsg
            self.estilo
           


if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Sala()
    janela.show()
    sys.exit(app.exec_())
