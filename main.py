from gui.GUI import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import docx

doc = docx.Document('./template.docx')
for p in doc:
    print(p)
app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())