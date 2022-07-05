# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from lokalizacijaDialog import Ui_Dialog
from fistulaDialog import Ui_fistulaDialog
from apscesiDialog import Ui_apscDialog

class Ui_MainWindow(object):
    def lokalizacijaDialog(self):
        if(self.drugoCheckBox.isChecked()):
            Dialog = QtWidgets.QDialog()
            ui = Ui_Dialog()
            ui.setupUi(Dialog)
            Dialog.show()
            self.drugoCheckBox.setChecked(False)
            Dialog.exec_()

    def fistulaDialog(self):
        if(self.fistDrugoCheckBox.isChecked()):
            fistulaDialog = QtWidgets.QDialog()
            ui = Ui_fistulaDialog()
            ui.setupUi(fistulaDialog)
            fistulaDialog.show()
            self.fistDrugoCheckBox.setChecked(False)
            fistulaDialog.exec_()
    def apscesiDialog(self):
        if(self.apscesDrugoCheckBox.isChecked()):
            apscDialog = QtWidgets.QDialog()
            ui = Ui_apscDialog()
            ui.setupUi(apscDialog)
            apscDialog.show()
            self.apscesDrugoCheckBox.setChecked(False)
            apscDialog.exec_()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(782, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dodajPoljaTab = QtWidgets.QTabWidget(self.centralwidget)
        self.dodajPoljaTab.setGeometry(QtCore.QRect(0, 0, 781, 871))
        self.dodajPoljaTab.setObjectName("dodajPoljaTab")
        self.OsnovniPodaci = QtWidgets.QWidget()
        self.OsnovniPodaci.setObjectName("OsnovniPodaci")
        self.label = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_5.setGeometry(QtCore.QRect(10, 110, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.OsnovniPodaci)
        self.line.setGeometry(QtCore.QRect(0, 140, 771, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.datumVazenjaZK = QtWidgets.QDateTimeEdit(self.OsnovniPodaci)
        self.datumVazenjaZK.setGeometry(QtCore.QRect(130, 110, 91, 21))
        self.datumVazenjaZK.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.Slovenia))
        self.datumVazenjaZK.setDate(QtCore.QDate(2022, 1, 1))
        self.datumVazenjaZK.setCalendarPopup(True)
        self.datumVazenjaZK.setObjectName("datumVazenjaZK")
        self.vidTerapijeCBox = QtWidgets.QComboBox(self.OsnovniPodaci)
        self.vidTerapijeCBox.setGeometry(QtCore.QRect(90, 160, 141, 22))
        self.vidTerapijeCBox.setObjectName("vidTerapijeCBox")
        self.vidTerapijeCBox.addItem("")
        self.vidTerapijeCBox.addItem("")
        self.vidTerapijeCBox.addItem("")
        self.vidTerapijeCBox.addItem("")
        self.label_7 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_7.setGeometry(QtCore.QRect(10, 190, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.M = QtWidgets.QRadioButton(self.OsnovniPodaci)
        self.M.setGeometry(QtCore.QRect(40, 190, 82, 17))
        self.M.setObjectName("M")
        self.Z = QtWidgets.QRadioButton(self.OsnovniPodaci)
        self.Z.setGeometry(QtCore.QRect(110, 190, 82, 17))
        self.Z.setChecked(True)
        self.Z.setObjectName("Z")
        self.label_8 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.godineZivota = QtWidgets.QSpinBox(self.OsnovniPodaci)
        self.godineZivota.setGeometry(QtCore.QRect(130, 220, 42, 22))
        self.godineZivota.setMinimum(1)
        self.godineZivota.setObjectName("godineZivota")
        self.label_9 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_9.setGeometry(QtCore.QRect(10, 250, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_10.setGeometry(QtCore.QRect(10, 280, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_11.setGeometry(QtCore.QRect(10, 310, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.izmeniOsnPodatkeDugme = QtWidgets.QPushButton(self.OsnovniPodaci)
        self.izmeniOsnPodatkeDugme.setGeometry(QtCore.QRect(300, 800, 181, 23))
        self.izmeniOsnPodatkeDugme.setObjectName("izmeniOsnPodatkeDugme")
        self.Ime = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.Ime.setGeometry(QtCore.QRect(130, 20, 131, 20))
        self.Ime.setObjectName("Ime")
        self.Prezime = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.Prezime.setGeometry(QtCore.QRect(130, 50, 131, 20))
        self.Prezime.setObjectName("Prezime")
        self.Filijala = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.Filijala.setGeometry(QtCore.QRect(130, 80, 131, 20))
        self.Filijala.setObjectName("Filijala")
        self.TM = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.TM.setGeometry(QtCore.QRect(130, 250, 131, 20))
        self.TM.setObjectName("TM")
        self.TV = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.TV.setGeometry(QtCore.QRect(130, 280, 131, 20))
        self.TV.setObjectName("TV")
        self.BMI = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.BMI.setGeometry(QtCore.QRect(130, 310, 131, 20))
        self.BMI.setObjectName("BMI")
        self.line_2 = QtWidgets.QFrame(self.OsnovniPodaci)
        self.line_2.setGeometry(QtCore.QRect(0, 340, 771, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_12 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_12.setGeometry(QtCore.QRect(10, 360, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_13.setGeometry(QtCore.QRect(10, 390, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_14.setGeometry(QtCore.QRect(10, 420, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_15.setGeometry(QtCore.QRect(10, 450, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_16.setGeometry(QtCore.QRect(10, 480, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_17.setGeometry(QtCore.QRect(10, 510, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_19 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_19.setGeometry(QtCore.QRect(10, 540, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.kAktBolestiCBox = QtWidgets.QComboBox(self.OsnovniPodaci)
        self.kAktBolestiCBox.setGeometry(QtCore.QRect(160, 540, 81, 22))
        self.kAktBolestiCBox.setObjectName("kAktBolestiCBox")
        self.kAktBolestiCBox.addItem("")
        self.kAktBolestiCBox.addItem("")
        self.kAktBolestiCBox.addItem("")
        self.kAktBolestiCBox.addItem("")
        self.label_20 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_20.setGeometry(QtCore.QRect(10, 600, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.CRP = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.CRP.setGeometry(QtCore.QRect(170, 600, 131, 20))
        self.CRP.setObjectName("CRP")
        self.label_21 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_21.setGeometry(QtCore.QRect(10, 630, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.fekalniKal = QtWidgets.QLineEdit(self.OsnovniPodaci)
        self.fekalniKal.setGeometry(QtCore.QRect(170, 630, 131, 20))
        self.fekalniKal.setObjectName("fekalniKal")
        self.label_22 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_22.setGeometry(QtCore.QRect(10, 660, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_22.setFont(font)
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_23.setGeometry(QtCore.QRect(10, 690, 141, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_23.setFont(font)
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_24.setGeometry(QtCore.QRect(10, 720, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_24.setFont(font)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_25.setGeometry(QtCore.QRect(10, 750, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_25.setFont(font)
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_26.setGeometry(QtCore.QRect(490, 610, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.OsnovniPodaci)
        self.label_27.setGeometry(QtCore.QRect(490, 680, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setObjectName("label_27")
        self.qgGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.qgGroupBox.setGeometry(QtCore.QRect(170, 660, 211, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.qgGroupBox.setFont(font)
        self.qgGroupBox.setTitle("")
        self.qgGroupBox.setFlat(True)
        self.qgGroupBox.setObjectName("qgGroupBox")
        self.qgNeg = QtWidgets.QRadioButton(self.qgGroupBox)
        self.qgNeg.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.qgNeg.setAutoExclusive(True)
        self.qgNeg.setObjectName("qgNeg")
        self.qgPoz = QtWidgets.QRadioButton(self.qgGroupBox)
        self.qgPoz.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.qgPoz.setAutoExclusive(True)
        self.qgPoz.setObjectName("qgPoz")
        self.rtgGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.rtgGroupBox.setGeometry(QtCore.QRect(170, 690, 211, 31))
        self.rtgGroupBox.setTitle("")
        self.rtgGroupBox.setFlat(True)
        self.rtgGroupBox.setObjectName("rtgGroupBox")
        self.rtgUredan = QtWidgets.QRadioButton(self.rtgGroupBox)
        self.rtgUredan.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.rtgUredan.setAutoExclusive(True)
        self.rtgUredan.setObjectName("rtgUredan")
        self.rtgIzmenjen = QtWidgets.QRadioButton(self.rtgGroupBox)
        self.rtgIzmenjen.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.rtgIzmenjen.setAutoExclusive(True)
        self.rtgIzmenjen.setObjectName("rtgIzmenjen")
        self.hbGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.hbGroupBox.setGeometry(QtCore.QRect(170, 750, 211, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.hbGroupBox.setFont(font)
        self.hbGroupBox.setTitle("")
        self.hbGroupBox.setFlat(True)
        self.hbGroupBox.setObjectName("hbGroupBox")
        self.hbNeg = QtWidgets.QRadioButton(self.hbGroupBox)
        self.hbNeg.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.hbNeg.setAutoExclusive(True)
        self.hbNeg.setObjectName("hbNeg")
        self.hbPoz = QtWidgets.QRadioButton(self.hbGroupBox)
        self.hbPoz.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.hbPoz.setAutoExclusive(True)
        self.hbPoz.setObjectName("hbPoz")
        self.testClostGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.testClostGroupBox.setGeometry(QtCore.QRect(170, 720, 211, 20))
        font = QtGui.QFont()
        font.setKerning(True)
        self.testClostGroupBox.setFont(font)
        self.testClostGroupBox.setTitle("")
        self.testClostGroupBox.setFlat(True)
        self.testClostGroupBox.setObjectName("testClostGroupBox")
        self.testNeg = QtWidgets.QRadioButton(self.testClostGroupBox)
        self.testNeg.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.testNeg.setAutoExclusive(True)
        self.testNeg.setObjectName("testNeg")
        self.testPoz = QtWidgets.QRadioButton(self.testClostGroupBox)
        self.testPoz.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.testPoz.setAutoExclusive(True)
        self.testPoz.setObjectName("testPoz")
        self.endoskopGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.endoskopGroupBox.setGeometry(QtCore.QRect(650, 610, 121, 41))
        self.endoskopGroupBox.setTitle("")
        self.endoskopGroupBox.setFlat(True)
        self.endoskopGroupBox.setObjectName("endoskopGroupBox")
        self.endoPrisustvo = QtWidgets.QRadioButton(self.endoskopGroupBox)
        self.endoPrisustvo.setGeometry(QtCore.QRect(0, 0, 121, 17))
        self.endoPrisustvo.setAutoExclusive(True)
        self.endoPrisustvo.setObjectName("endoPrisustvo")
        self.endoOdsustvo = QtWidgets.QRadioButton(self.endoskopGroupBox)
        self.endoOdsustvo.setGeometry(QtCore.QRect(0, 20, 121, 17))
        self.endoOdsustvo.setAutoExclusive(True)
        self.endoOdsustvo.setObjectName("endoOdsustvo")
        self.operacijaGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.operacijaGroupBox.setGeometry(QtCore.QRect(650, 680, 101, 21))
        self.operacijaGroupBox.setTitle("")
        self.operacijaGroupBox.setFlat(True)
        self.operacijaGroupBox.setObjectName("operacijaGroupBox")
        self.opNe = QtWidgets.QRadioButton(self.operacijaGroupBox)
        self.opNe.setGeometry(QtCore.QRect(0, 0, 41, 17))
        self.opNe.setAutoExclusive(True)
        self.opNe.setObjectName("opNe")
        self.opDa = QtWidgets.QRadioButton(self.operacijaGroupBox)
        self.opDa.setGeometry(QtCore.QRect(50, 0, 41, 17))
        self.opDa.setAutoExclusive(True)
        self.opDa.setObjectName("opDa")
        self.line_3 = QtWidgets.QFrame(self.OsnovniPodaci)
        self.line_3.setGeometry(QtCore.QRect(0, 590, 771, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lokalizacijaGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.lokalizacijaGroupBox.setGeometry(QtCore.QRect(80, 350, 531, 31))
        self.lokalizacijaGroupBox.setTitle("")
        self.lokalizacijaGroupBox.setFlat(True)
        self.lokalizacijaGroupBox.setObjectName("lokalizacijaGroupBox")
        self.ileumcheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.ileumcheckBox.setGeometry(QtCore.QRect(0, 10, 51, 17))
        self.ileumcheckBox.setObjectName("ileumcheckBox")
        self.ileumkolonCheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.ileumkolonCheckBox.setGeometry(QtCore.QRect(50, 10, 91, 17))
        self.ileumkolonCheckBox.setObjectName("ileumkolonCheckBox")
        self.kolonCheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.kolonCheckBox.setGeometry(QtCore.QRect(140, 10, 51, 17))
        self.kolonCheckBox.setObjectName("kolonCheckBox")
        self.rektumCheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.rektumCheckBox.setGeometry(QtCore.QRect(190, 10, 61, 17))
        self.rektumCheckBox.setObjectName("rektumCheckBox")
        self.proksSegCheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.proksSegCheckBox.setGeometry(QtCore.QRect(250, 10, 171, 17))
        self.proksSegCheckBox.setObjectName("proksSegCheckBox")
        self.drugoCheckBox = QtWidgets.QCheckBox(self.lokalizacijaGroupBox)
        self.drugoCheckBox.setGeometry(QtCore.QRect(420, 10, 70, 17))
        self.drugoCheckBox.setObjectName("drugoCheckBox")
        self.datumTrajanja = QtWidgets.QDateEdit(self.OsnovniPodaci)
        self.datumTrajanja.setGeometry(QtCore.QRect(160, 480, 61, 22))
        self.datumTrajanja.setObjectName("datumTrajanja")
        self.datumEndo = QtWidgets.QDateTimeEdit(self.OsnovniPodaci)
        self.datumEndo.setGeometry(QtCore.QRect(650, 650, 121, 22))
        self.datumEndo.setObjectName("datumEndo")
        self.ponasanjeGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.ponasanjeGroupBox.setGeometry(QtCore.QRect(120, 390, 411, 21))
        self.ponasanjeGroupBox.setTitle("")
        self.ponasanjeGroupBox.setFlat(True)
        self.ponasanjeGroupBox.setObjectName("ponasanjeGroupBox")
        self.inflmCheckBox = QtWidgets.QCheckBox(self.ponasanjeGroupBox)
        self.inflmCheckBox.setGeometry(QtCore.QRect(0, 0, 111, 17))
        self.inflmCheckBox.setObjectName("inflmCheckBox")
        self.penetrCheckBox = QtWidgets.QCheckBox(self.ponasanjeGroupBox)
        self.penetrCheckBox.setGeometry(QtCore.QRect(120, 0, 81, 17))
        self.penetrCheckBox.setObjectName("penetrCheckBox")
        self.stenoCheckBox = QtWidgets.QCheckBox(self.ponasanjeGroupBox)
        self.stenoCheckBox.setGeometry(QtCore.QRect(210, 0, 81, 17))
        self.stenoCheckBox.setObjectName("stenoCheckBox")
        self.fistulaGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.fistulaGroupBox.setGeometry(QtCore.QRect(70, 410, 81, 31))
        self.fistulaGroupBox.setTitle("")
        self.fistulaGroupBox.setFlat(True)
        self.fistulaGroupBox.setObjectName("fistulaGroupBox")
        self.fistulaDa = QtWidgets.QRadioButton(self.fistulaGroupBox)
        self.fistulaDa.setGeometry(QtCore.QRect(0, 10, 41, 17))
        self.fistulaDa.setObjectName("fistulaDa")
        self.fistulaNe = QtWidgets.QRadioButton(self.fistulaGroupBox)
        self.fistulaNe.setGeometry(QtCore.QRect(40, 10, 31, 17))
        self.fistulaNe.setObjectName("fistulaNe")
        self.apscesiGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.apscesiGroupBox.setGeometry(QtCore.QRect(70, 440, 81, 31))
        self.apscesiGroupBox.setTitle("")
        self.apscesiGroupBox.setFlat(True)
        self.apscesiGroupBox.setObjectName("apscesiGroupBox")
        self.apscDa = QtWidgets.QRadioButton(self.apscesiGroupBox)
        self.apscDa.setGeometry(QtCore.QRect(0, 10, 41, 17))
        self.apscDa.setObjectName("apscDa")
        self.apscNe = QtWidgets.QRadioButton(self.apscesiGroupBox)
        self.apscNe.setGeometry(QtCore.QRect(40, 10, 31, 17))
        self.apscNe.setObjectName("apscNe")
        self.eimGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.eimGroupBox.setGeometry(QtCore.QRect(160, 500, 81, 31))
        self.eimGroupBox.setTitle("")
        self.eimGroupBox.setFlat(True)
        self.eimGroupBox.setObjectName("eimGroupBox")
        self.eimNe = QtWidgets.QRadioButton(self.eimGroupBox)
        self.eimNe.setGeometry(QtCore.QRect(0, 10, 41, 17))
        self.eimNe.setObjectName("eimNe")
        self.eimDa = QtWidgets.QRadioButton(self.eimGroupBox)
        self.eimDa.setGeometry(QtCore.QRect(40, 10, 31, 17))
        self.eimDa.setObjectName("eimDa")
        self.fistulaHiddenGroupBox = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.fistulaHiddenGroupBox.setGeometry(QtCore.QRect(160, 410, 581, 31))
        self.fistulaHiddenGroupBox.setFlat(True)
        self.fistulaHiddenGroupBox.setObjectName("fistulaHiddenGroupBox")
        self.periAnCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.periAnCheckBox.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.periAnCheckBox.setObjectName("periAnCheckBox")
        self.enteroKutCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.enteroKutCheckBox.setGeometry(QtCore.QRect(90, 10, 91, 17))
        self.enteroKutCheckBox.setObjectName("enteroKutCheckBox")
        self.enteroVagCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.enteroVagCheckBox.setGeometry(QtCore.QRect(180, 10, 101, 17))
        self.enteroVagCheckBox.setObjectName("enteroVagCheckBox")
        self.enteroEntCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.enteroEntCheckBox.setGeometry(QtCore.QRect(290, 10, 101, 17))
        self.enteroEntCheckBox.setObjectName("enteroEntCheckBox")
        self.enteroVezCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.enteroVezCheckBox.setGeometry(QtCore.QRect(400, 10, 101, 17))
        self.enteroVezCheckBox.setObjectName("enteroVezCheckBox")
        self.fistDrugoCheckBox = QtWidgets.QCheckBox(self.fistulaHiddenGroupBox)
        self.fistDrugoCheckBox.setGeometry(QtCore.QRect(500, 10, 70, 17))
        self.fistDrugoCheckBox.setObjectName("fistDrugoCheckBox")
        self.apscesHiddenGroupBox_2 = QtWidgets.QGroupBox(self.OsnovniPodaci)
        self.apscesHiddenGroupBox_2.setGeometry(QtCore.QRect(160, 440, 251, 31))
        self.apscesHiddenGroupBox_2.setFlat(True)
        self.apscesHiddenGroupBox_2.setObjectName("apscesHiddenGroupBox_2")
        self.periAnApscesCheckBox = QtWidgets.QCheckBox(self.apscesHiddenGroupBox_2)
        self.periAnApscesCheckBox.setGeometry(QtCore.QRect(10, 10, 70, 17))
        self.periAnApscesCheckBox.setObjectName("periAnApscesCheckBox")
        self.interIntCheckBox = QtWidgets.QCheckBox(self.apscesHiddenGroupBox_2)
        self.interIntCheckBox.setGeometry(QtCore.QRect(90, 10, 101, 17))
        self.interIntCheckBox.setObjectName("interIntCheckBox")
        self.apscesDrugoCheckBox = QtWidgets.QCheckBox(self.apscesHiddenGroupBox_2)
        self.apscesDrugoCheckBox.setGeometry(QtCore.QRect(200, 10, 51, 17))
        self.apscesDrugoCheckBox.setObjectName("apscesDrugoCheckBox")
        self.dodajPoljaTab.addTab(self.OsnovniPodaci, "")
        self.dodajPoljaTab1 = QtWidgets.QWidget()
        self.dodajPoljaTab1.setObjectName("dodajPoljaTab1")
        self.dodajPoljeDugme = QtWidgets.QPushButton(self.dodajPoljaTab1)
        self.dodajPoljeDugme.setGeometry(QtCore.QRect(340, 790, 91, 31))
        self.dodajPoljeDugme.setObjectName("dodajPoljeDugme")
        self.dodajPoljaTab.addTab(self.dodajPoljaTab1, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.dodajPoljaTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.drugoCheckBox.stateChanged.connect(self.lokalizacijaDialog)
        self.apscesDrugoCheckBox.stateChanged.connect(self.apscesiDialog)
        self.fistDrugoCheckBox.stateChanged.connect(self.fistulaDialog)
        self.fistulaDa.toggled.connect(self.fistulaHiddenGroupBox.show)
        self.apscDa.toggled.connect(self.apscesHiddenGroupBox_2.show)
        self.fistulaNe.toggled.connect(self.fistulaHiddenGroupBox.hide)
        self.apscNe.toggled.connect(self.apscesHiddenGroupBox_2.hide)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Klinicki Centar Helper"))
        self.label.setText(_translate("MainWindow", "Ime"))
        self.label_2.setText(_translate("MainWindow", "Prezime"))
        self.label_4.setText(_translate("MainWindow", "Filijala"))
        self.label_5.setText(_translate("MainWindow", "Datum važenja Z.K."))
        self.label_6.setText(_translate("MainWindow", "Vid terapije"))
        self.datumVazenjaZK.setDisplayFormat(_translate("MainWindow", "dd/MM/yyyy"))
        self.vidTerapijeCBox.setItemText(0, _translate("MainWindow", "Uvođenje leka u terapiju"))
        self.vidTerapijeCBox.setItemText(1, _translate("MainWindow", "Terapije održavanja"))
        self.vidTerapijeCBox.setItemText(2, _translate("MainWindow", "Promena leka"))
        self.vidTerapijeCBox.setItemText(3, _translate("MainWindow", "Prekid terapije"))
        self.label_7.setText(_translate("MainWindow", "Pol"))
        self.M.setText(_translate("MainWindow", "Muški"))
        self.Z.setText(_translate("MainWindow", "Ženski"))
        self.label_8.setText(_translate("MainWindow", "Godine života"))
        self.label_9.setText(_translate("MainWindow", "TM"))
        self.label_10.setText(_translate("MainWindow", "TV"))
        self.label_11.setText(_translate("MainWindow", "BMI"))
        self.izmeniOsnPodatkeDugme.setText(_translate("MainWindow", "Izmeni"))
        self.label_12.setText(_translate("MainWindow", "Lokalizacija"))
        self.label_13.setText(_translate("MainWindow", "Ponašanje bolesti"))
        self.label_14.setText(_translate("MainWindow", "Fistula/e"))
        self.label_15.setText(_translate("MainWindow", "Apsces/-i"))
        self.label_16.setText(_translate("MainWindow", "Dužina trajanja bolesti od"))
        self.label_17.setText(_translate("MainWindow", "Ekstraint. manifestacije"))
        self.label_19.setText(_translate("MainWindow", "Klinička aktivnost bolesti"))
        self.kAktBolestiCBox.setItemText(0, _translate("MainWindow", "Blaga"))
        self.kAktBolestiCBox.setItemText(1, _translate("MainWindow", "Umerena"))
        self.kAktBolestiCBox.setItemText(2, _translate("MainWindow", "Izrazito aktivna"))
        self.kAktBolestiCBox.setItemText(3, _translate("MainWindow", "Remisija"))
        self.label_20.setText(_translate("MainWindow", "Vrednosti CRP"))
        self.label_21.setText(_translate("MainWindow", "Fekalni kalprotektin"))
        self.label_22.setText(_translate("MainWindow", "Quantiferon gold"))
        self.label_23.setText(_translate("MainWindow", "RTG srca i pluća"))
        self.label_24.setText(_translate("MainWindow", "Test na Clostridium difficile"))
        self.label_25.setText(_translate("MainWindow", "HBs antigen"))
        self.label_26.setText(_translate("MainWindow", "Endoskopija"))
        self.label_27.setText(_translate("MainWindow", "Operacija"))
        self.qgNeg.setText(_translate("MainWindow", "Negativan"))
        self.qgPoz.setText(_translate("MainWindow", "Pozitivan"))
        self.rtgUredan.setText(_translate("MainWindow", "Nalaz uredan"))
        self.rtgIzmenjen.setText(_translate("MainWindow", "Izmenjen"))
        self.hbNeg.setText(_translate("MainWindow", "Negativan"))
        self.hbPoz.setText(_translate("MainWindow", "Pozitivan"))
        self.testNeg.setText(_translate("MainWindow", "Negativan"))
        self.testPoz.setText(_translate("MainWindow", "Pozitivan"))
        self.endoPrisustvo.setText(_translate("MainWindow", "Prisustvo ulceracija"))
        self.endoOdsustvo.setText(_translate("MainWindow", "Odsustvo ulceracija"))
        self.opNe.setText(_translate("MainWindow", "Ne"))
        self.opDa.setText(_translate("MainWindow", "Da"))
        self.ileumcheckBox.setText(_translate("MainWindow", "Ileum"))
        self.ileumkolonCheckBox.setText(_translate("MainWindow", "Ileum + Kolon"))
        self.kolonCheckBox.setText(_translate("MainWindow", "Kolon"))
        self.rektumCheckBox.setText(_translate("MainWindow", "Rektum"))
        self.proksSegCheckBox.setText(_translate("MainWindow", "Proksimalni segmenti GI trakta"))
        self.drugoCheckBox.setText(_translate("MainWindow", "Drugo"))
        self.datumTrajanja.setDisplayFormat(_translate("MainWindow", "yyyy"))
        self.datumEndo.setDisplayFormat(_translate("MainWindow", "MM/yyyy"))
        self.inflmCheckBox.setText(_translate("MainWindow", "Inflamatorna forma"))
        self.penetrCheckBox.setText(_translate("MainWindow", "Penetrantna"))
        self.stenoCheckBox.setText(_translate("MainWindow", "Stenozantna"))
        self.fistulaDa.setText(_translate("MainWindow", "Da"))
        self.fistulaNe.setText(_translate("MainWindow", "Ne"))
        self.apscDa.setText(_translate("MainWindow", "Da"))
        self.apscNe.setText(_translate("MainWindow", "Ne"))
        self.eimNe.setText(_translate("MainWindow", "Da"))
        self.eimDa.setText(_translate("MainWindow", "Ne"))
        self.fistulaHiddenGroupBox.setTitle(_translate("MainWindow", "Fistula/e"))
        self.periAnCheckBox.setText(_translate("MainWindow", "Perianalna"))
        self.enteroKutCheckBox.setText(_translate("MainWindow", "Enterokutana"))
        self.enteroVagCheckBox.setText(_translate("MainWindow", "Enterovaginalna"))
        self.enteroEntCheckBox.setText(_translate("MainWindow", "Enteroenteralna"))
        self.enteroVezCheckBox.setText(_translate("MainWindow", "Enterovezikalna"))
        self.fistDrugoCheckBox.setText(_translate("MainWindow", "Drugo"))
        self.apscesHiddenGroupBox_2.setTitle(_translate("MainWindow", "Apsces/-i"))
        self.periAnApscesCheckBox.setText(_translate("MainWindow", "Perianalni"))
        self.interIntCheckBox.setText(_translate("MainWindow", "Interintestinalni"))
        self.apscesDrugoCheckBox.setText(_translate("MainWindow", "Drugo"))
        self.dodajPoljaTab.setTabText(self.dodajPoljaTab.indexOf(self.OsnovniPodaci), _translate("MainWindow", "Osnovni podaci"))
        self.dodajPoljeDugme.setText(_translate("MainWindow", "Dodaj polje"))
        self.dodajPoljaTab.setTabText(self.dodajPoljaTab.indexOf(self.dodajPoljaTab1), _translate("MainWindow", "Dodaj polja"))
        self.fistulaHiddenGroupBox.hide()
        self.apscesHiddenGroupBox_2.hide()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
