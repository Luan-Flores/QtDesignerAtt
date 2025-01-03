# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SalaDeAula.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1020, 689)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(-100, -30, 1171, 721))
        self.imgLabel.setStyleSheet("")
        self.imgLabel.setText("")
        self.imgLabel.setPixmap(QtGui.QPixmap("crianca.jpg"))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName("imgLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 90, 571, 51))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(25)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.inputLabel = QtWidgets.QLineEdit(self.centralwidget)
        self.inputLabel.setGeometry(QtCore.QRect(310, 170, 341, 61))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.inputLabel.setFont(font)
        self.inputLabel.setStyleSheet("background-color: rgb(2, 85, 43);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(208, 185, 158);")
        self.inputLabel.setObjectName("inputLabel")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(330, 140, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 340, 521, 91))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(2, 85, 43);\n"
"color: rgb(255, 255, 255);\n"
"border: 3px solid rgb(208, 185, 158);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verifyBtn = QtWidgets.QPushButton(self.centralwidget)
        self.verifyBtn.setGeometry(QtCore.QRect(450, 280, 75, 23))
        self.verifyBtn.setStyleSheet("background-color: white; border-radius:20px;")
        self.verifyBtn.setObjectName("verifyBtn")
        self.labelResult = QtWidgets.QLabel(self.centralwidget)
        self.labelResult.setGeometry(QtCore.QRect(370, 340, 581, 91))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(9)
        self.labelResult.setFont(font)
        self.labelResult.setStyleSheet("color:white;")
        self.labelResult.setObjectName("labelResult")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(670, 120, 291, 261))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("curioso.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 21))
        self.menubar.setObjectName("menubar")
        self.menuSalvar = QtWidgets.QMenu(self.menubar)
        self.menuSalvar.setObjectName("menuSalvar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSalvar = QtWidgets.QAction(MainWindow)
        self.actionSalvar.setObjectName("actionSalvar")
        self.menuSalvar.addAction(self.actionSalvar)
        self.menubar.addAction(self.menuSalvar.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DIA DE AVALIAÇÃO!!!!"))
        self.label_2.setText(_translate("MainWindow", "Digite a nota de 0 a 100"))
        self.verifyBtn.setText(_translate("MainWindow", "Verificar!"))
        self.labelResult.setText(_translate("MainWindow", "90 ou + : Excelente\n"
"70 ou + : Bom\n"
"50 ou + : Regular\n"
"Menor que 50: Insuficiente\n"
""))
        self.menuSalvar.setTitle(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
