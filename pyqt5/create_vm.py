from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import sys


class CreateVm(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, val, rank, api):
        super(CreateVm,self).__init__()
        self.val = val
        self.rank = rank
        self.api = api

        self.l1 = QLineEdit()
        self.l2 = QLineEdit()


        self.createFormGroupBox()


        btn_ok = QPushButton("ok")
        btn_ok.clicked.connect(self.ok)


        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(btn_ok)
        self.setLayout(mainLayout)

        self.setWindowTitle("Create all vm for students")

    def createFormGroupBox(self):
        label = "VM " + self.val[self.rank]['hostname']
        self.formGroupBox = QGroupBox(label)
        layout = QFormLayout()
        layout.addRow(QLabel("VM Name"), self.l1 )
        layout.addRow(QLabel("Number"), self.l2)


        self.formGroupBox.setLayout(layout)
    def ok(self):
        print('clicked')
        name = self.l1.text()
        number = self.l2.text()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = CreateVm()
    sys.exit(dialog.exec_())
