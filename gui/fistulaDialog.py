# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fistulaDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fistulaDialog(object):
    def setupUi(self, fistulaDialog):
        fistulaDialog.setObjectName("fistulaDialog")
        fistulaDialog.resize(400, 300)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        fistulaDialog.setFont(font)
        self.label_2 = QtWidgets.QLabel(fistulaDialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.fistDialogText = QtWidgets.QPlainTextEdit(fistulaDialog)
        self.fistDialogText.setGeometry(QtCore.QRect(10, 20, 381, 251))
        self.fistDialogText.setObjectName("fistDialogText")
        self.fistOKButton = QtWidgets.QPushButton(fistulaDialog)
        self.fistOKButton.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.fistOKButton.setObjectName("fistOKButton")

        self.retranslateUi(fistulaDialog)
        QtCore.QMetaObject.connectSlotsByName(fistulaDialog)

    def retranslateUi(self, fistulaDialog):
        _translate = QtCore.QCoreApplication.translate
        fistulaDialog.setWindowTitle(_translate("fistulaDialog", "Ostale fistule"))
        self.label_2.setText(_translate("fistulaDialog", "Druge fistule upisati uredno ovde!"))
        self.fistOKButton.setText(_translate("fistulaDialog", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fistulaDialog = QtWidgets.QDialog()
    ui = Ui_fistulaDialog()
    ui.setupUi(fistulaDialog)
    fistulaDialog.show()
    sys.exit(app.exec_())