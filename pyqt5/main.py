import sys
from time import sleep
from lndynamic import LNDynamic
from dialog import Dialog

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QListWidget,

)

with open(r"../../../system-dev.txt") as hpass:
    lines = hpass.readlines()

api = LNDynamic(lines[0].rstrip('\n'), lines[1].rstrip('\n'))


class Window(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clicksCount = 0
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Luna-manager")
        self.resize(300, 150)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)


        self.listwidget = QListWidget()
        self.results = api.request('vm', 'list')
        self.val = self.results.get('vms')
        i = 0
        for item in self.val:
            self.listwidget.insertItem(i,item['name'])
            i += 1
        self.listwidget.clicked.connect(self.clicked)
        layout = QVBoxLayout()
        layout.addWidget(self.listwidget)
        self.centralWidget.setLayout(layout)

    def clicked(self, qmodelindex):
        rank = self.listwidget.currentRow()
        dialog = Dialog(self.val,rank, api)
        dialog.exec_()


    def countClicks(self):
        self.clicksCount += 1
        self.clicksLabel.setText(f"Counting: {self.clicksCount} clicks")

    def reportProgress(self, n):
        self.stepLabel.setText(f"Long-Running Step: {n}")

    def runLongTask(self):
        """Long-running task in 5 steps."""
        for i in range(5):
            sleep(1)
            self.reportProgress(i + 1)

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec())
