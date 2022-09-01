from PyQt5.QtWidgets import QApplication,QLineEdit,QWidget,QFormLayout
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QFont
from PyQt5.QtCore import Qt
import sys

class lineEditDemo(QWidget):
        def __init__(self,val,rank,parent=None):
                super().__init__(parent)
                l1 = QLineEdit(val[rank]['plan_id'])
                l1.setReadOnly(True)

                l2 = QLineEdit(val[rank]['vm_id'])
                l2.setReadOnly(True)

                l3 = QLineEdit(val[rank]['hostname'])
                l3.setReadOnly(True)
                l4 = QLineEdit(val[rank]['primaryip'])
                l4.setReadOnly(True)

                l5 = QLineEdit(val[rank]['privateip'])
                l5.setReadOnly(True)

                l6 = QLineEdit(val[rank]['ram'])
                l6.setReadOnly(True)

                l7 = QLineEdit(val[rank]['vcpu'])
                l7.setReadOnly(True)

                l8 = QLineEdit(val[rank]['storage'])
                l8.setReadOnly(True)

                l9 = QLineEdit(val[rank]['region'])
                l9.setReadOnly(True)

                l10 = QLineEdit(val[rank]['os_status'])
                l10.setReadOnly(True)

                flo = QFormLayout()
                flo.addRow("plan_id",l1)
                flo.addRow("vm_id",l2)
                flo.addRow("hostname",l3)
                flo.addRow("primaryip",l4)
                flo.addRow("privateip",l5)
                flo.addRow("ram",l6)
                flo.addRow("vcpu", l7)
                flo.addRow("storage", l8)
                flo.addRow("region", l9)
                flo.addRow("os_status", l10)

                self.setLayout(flo)
                self.setWindowTitle("VM Details")

        def textchanged(self,text):
                print("Changed: " + text)

        def enterPress(self):
                print("Enter pressed")

if __name__ == "__main__":
        app = QApplication(sys.argv)
        win = lineEditDemo()
        win.show()
        sys.exit(app.exec_())