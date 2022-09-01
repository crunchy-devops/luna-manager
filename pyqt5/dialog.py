from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

import sys
from create_vm import CreateVm

class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self, val, rank, api):
        super(Dialog,self).__init__()
        self.val = val
        self.rank = rank
        self.api = api

        self.l1 = QLineEdit(val[rank]['plan_id'])
        self.l1.setReadOnly(True)

        self.l2 = QLineEdit(val[rank]['vm_id'])
        self.l2.setMaxLength(50)
        self.l2.setReadOnly(True)

        self.l3 = QLineEdit(val[rank]['hostname'])
        self.l3.setReadOnly(True)
        self.l4 = QLineEdit(val[rank]['primaryip'])
        self.l4.setReadOnly(True)

        self.l5 = QLineEdit(val[rank]['privateip'])
        self.l5.setReadOnly(True)

        self.l6 = QLineEdit(val[rank]['ram'])
        self.l6.setReadOnly(True)

        self.l7 = QLineEdit(val[rank]['vcpu'])
        self.l7.setReadOnly(True)

        self.l8 = QLineEdit(val[rank]['storage'])
        self.l8.setReadOnly(True)

        self.l9 = QLineEdit(val[rank]['region'])
        self.l9.setReadOnly(True)

        self.l10 = QLineEdit(val[rank]['os_status'])
        self.l10.setReadOnly(True)

        self.createFormGroupBox()


        simple = QPushButton("Simple VM")
        master = QPushButton("Master/Node")
        cancel = QPushButton("Cancel")
        simple.clicked.connect(self.vmrole)
        master.clicked.connect(self.noderole)
        cancel.clicked.connect(self.close_clicked)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(simple)
        mainLayout.addWidget(master)
        mainLayout.addWidget(cancel)
        self.setLayout(mainLayout)

        self.setWindowTitle("Vm Detail")

    def createFormGroupBox(self):
        label = "VM " + self.val[self.rank]['hostname']
        self.formGroupBox = QGroupBox(label)
        layout = QFormLayout()
        layout.addRow(QLabel("Plan_id:"), self.l1 )
        layout.addRow(QLabel("vm_id:"), self.l2)
        layout.addRow(QLabel("hostname:"), self.l3)
        layout.addRow(QLabel("primaryip:"), self.l4)
        layout.addRow(QLabel("privateip:"), self.l5)
        layout.addRow(QLabel("ram:"), self.l6)
        layout.addRow(QLabel("vcpu:"), self.l7)
        layout.addRow(QLabel("storage:"), self.l8)
        layout.addRow(QLabel("region:"), self.l9)
        layout.addRow(QLabel("os_status:"), self.l10)

        self.formGroupBox.setLayout(layout)
    def vmrole(self):

        dialog = CreateVm(self.val, self.rank, self.api)
        dialog.exec_()

    def noderole(self):
        print("clicked")

    def close_clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    sys.exit(dialog.exec_())
