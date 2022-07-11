import string
from tokenize import String
from gui.GUI import Ui_MainWindow
from gui.GUI import Ui_apscDialog
from gui.GUI import Ui_fistulaDialog
from gui.GUI import Ui_Dialog

class osnovniPojmovi(Ui_MainWindow):
    ime = prezime = filijala = ""
    godineZivota = tm = tv = 0                      # tm = kg, tv = cm
    bmi = crp = kalProt = 0.                        # kg/m2
    lokalizacije = []
    ponasanjeBolesti = []
    fistule = []
    apscesi = []
    duzinaTrajanja = []
    def setIme(self):
        self.ime = Ui_MainWindow.getIme()



osnovniPojmovi.setIme()
