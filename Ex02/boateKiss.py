

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1095, 829)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(-10, 0, 1121, 801))
        self.imgLabel.setText("")
        self.imgLabel.setPixmap(QtGui.QPixmap("seguranca.jpg"))
        self.imgLabel.setScaledContents(True)
        self.imgLabel.setObjectName("imgLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1095, 21))
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
        self.menuSalvar.setTitle(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setText(_translate("MainWindow", "Salvar"))
        self.actionSalvar.setShortcut(_translate("MainWindow", "Ctrl+S"))
