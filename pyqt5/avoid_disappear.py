from PyQt5 import QtCore, QtGui, QtWidgets
from lndynamic import LNDynamic
from form import lineEditDemo


with open(r"../../../system-dev.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(557, 383)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.listwidget = QtWidgets.QListWidget(self.centralwidget)
        self.results = api.request('vm', 'list')
        self.val = self.results.get('vms')
        i = 0
        for item in self.val:
            self.listwidget.insertItem(i, item['name'])
            i += 1
        self.listwidget.clicked.connect(self.newWindow)
        # layout.addWidget(self.clicksLabel)
        # layout.addWidget(self.countBtn)
        # layout.addStretch()
        # layout.addWidget(self.stepLabel)
        # layout.addWidget(self.longRunningBtn)


        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(180, 70, 201, 81))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.newWindow)


        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 557, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "new window"))

    """ 
    def newWindow(self):
        self.dialog = QtWidgets.QDialog() 
        self.myOtherWindow = Ui_Dialog()
        self.myOtherWindow.setupUi(self.dialog)
        self.dialog.show()
    """

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    def newWindow(self):
        rank = self.listwidget.currentRow()
        win = lineEditDemo(self.val, rank)
        win.show()
        dialog = QtWidgets.QDialog()
        #dialog.setWindowTitle("Dialog")
        #dialog.setGeometry(800, 300, 400, 300)
        #dialog.exec_()


if __name__ == "__main__":
    import sys
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())