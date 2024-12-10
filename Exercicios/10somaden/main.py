import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from somaden import Ui_MainWindow  # Importa a interface gerada

class Somaden(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Conectar o botão à função que realiza a soma
        self.ui.botao.clicked.connect(self.somaTudo)

    def somaTudo(self):
        myList=[]
        num=int(self.ui.input.text())
        for i in range(num+1):
            myList.append(i)
        result=sum(myList)
        print(f'Soma de 1 até {num} ---> {result}')

        
        try:
            self.ui.resultado.setText(f"Resultado: {result}")
            
        except ValueError:
            self.ui.resultado.setText("Por favor, insira números válidos!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Somaden()
    janela.show()
    sys.exit(app.exec_())
