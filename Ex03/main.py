import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimedia import QSound
from piano import Ui_MainWindow  # Importa a interface gerada

class Piano(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.notaText.setText(f"")
           # Obter referência ao botão de liga/desliga
        self.ligarBtn = self.ui.ligarBtn
        self.ligarBtn.setCheckable(True)
        self.ligarBtn.setChecked(False)  # Estado inicial: desligado
        self.ligarBtn.clicked.connect(self.atualizar_estado)


         # Conectar botões às funções
        
        self.ui.Do.clicked.connect(lambda: self.tocar('C'))
        self.ui.Do.clicked.connect(lambda: self.tocar_nota("C.wav"))
        self.ui.DoSustenido.clicked.connect(lambda: self.tocar_nota("C#.wav"))
        self.ui.Re.clicked.connect(lambda: self.tocar_nota("D.wav"))
        self.ui.ReSustenido.clicked.connect(lambda: self.tocar_nota("D#.wav"))
        self.ui.Mi.clicked.connect(lambda: self.tocar_nota("E.wav"))
        self.ui.Fa.clicked.connect(lambda: self.tocar_nota("F.wav"))
        self.ui.FaSustenido.clicked.connect(lambda: self.tocar_nota("F#.wav"))
        self.ui.Sol.clicked.connect(lambda: self.tocar_nota("G.wav"))
        self.ui.SolSustenido.clicked.connect(lambda: self.tocar_nota("G#.wav"))
        self.ui.La.clicked.connect(lambda: self.tocar_nota("A.wav"))
        self.ui.LaSustenido.clicked.connect(lambda: self.tocar_nota("A#.wav"))
        self.ui.Si.clicked.connect(lambda: self.tocar_nota("B.wav"))
        self.ui.DoSustenido.clicked.connect(lambda: self.tocar('C#'))
        self.ui.Re.clicked.connect(lambda: self.tocar('D'))
        self.ui.ReSustenido.clicked.connect(lambda: self.tocar('D#'))
        self.ui.Mi.clicked.connect(lambda: self.tocar('E'))
        self.ui.Fa.clicked.connect(lambda: self.tocar('F'))
        self.ui.FaSustenido.clicked.connect(lambda: self.tocar('F#'))
        self.ui.Sol.clicked.connect(lambda: self.tocar('G'))
        self.ui.SolSustenido.clicked.connect(lambda: self.tocar('G#'))
        self.ui.La.clicked.connect(lambda: self.tocar('A'))
        self.ui.LaSustenido.clicked.connect(lambda: self.tocar('A#'))
        self.ui.Si.clicked.connect(lambda: self.tocar('B'))
        
        # funcao para mostrar a nota tocada 
    def tocar(self, nota):
        # exibe a nota apenas se o botao estiver ligado
        if self.ligarBtn.isChecked():
            self.ui.notaText.setText(nota)
            
        else:
            self.ui.notaText.setText("")  # limpar o texto se o botão estiver desligado

    def atualizar_estado(self):
        # atualizar o estado do botão de liga/desliga
        if self.ligarBtn.isChecked():
            self.ligarBtn.setText("Ligado")
        else:
            self.ligarBtn.setText("Desligado")
            self.ui.notaText.setText("")  # limpar o texto da nota ao desligar

    def tocar_nota(self, arquivo_som):
        # Reproduzir som usando QSound (se o botão estiver ligado)
        if self.ligarBtn.isChecked():
            QSound.play(arquivo_som)
            
        else:
            self.ui.notaText.setText("")  # limpar o texto se o botão estiver desligado



if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = Piano()
    janela.show()
    sys.exit(app.exec_())
