# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manifestacijeDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ManifestacijeDialog(object):
    opis_Manifest = ''
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 261, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.manifestDialogText = QtWidgets.QPlainTextEdit(Dialog)
        self.manifestDialogText.setGeometry(QtCore.QRect(10, 20, 381, 251))
        self.manifestDialogText.setObjectName("manifestDialogText")
        self.manifestOKButton = QtWidgets.QPushButton(Dialog)
        self.manifestOKButton.setGeometry(QtCore.QRect(160, 270, 75, 23))
        self.manifestOKButton.setObjectName("manifestOKButton")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 270, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.manifestOKButton.clicked.connect(self.getText)
        self.pushButton.clicked.connect(Dialog.close)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "Opis dati ovde!"))
        self.manifestOKButton.setText(_translate("Dialog", "OK"))
        self.pushButton.setText(_translate("Dialog", "Izlaz!"))

    def getText(self):
        self.opis_Manifest = self.manifestDialogText.toPlainText()
        self.manifestOKButton.setEnabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_ManifestacijeDialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())