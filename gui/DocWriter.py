import docx
from docx.shared import Cm



def docWriting(data):
    doc = docx.Document()

    #margins
    doc.sections[0].top_margin = Cm(1)
    doc.sections[0].bottom_margin = Cm(1)
    doc.sections[0].left_margin = Cm(3)
    doc.sections[0].right_margin = Cm(2)

    #title
    doc.add_paragraph().add_run('FORMULAR ZA PRIMENU BIOLOŠKE TERAPIJE KOD PACIJENATA SA CROHN-OVOM BOLEŠĆU')

    # 1. Cluster
    #IME, JMBG, LBO, FILIJALA, KNJIZICA, USTANOVA
    para = doc.add_paragraph()
    para.add_run(f'Ime i prezime: {data["ime"]}\n')
    lin = para.add_run(f'JMBG: {data["jmbg"]}\t\t')
    lin.add_text(f'LBO: {data["lbo"]}\t')
    lin.add_text(f'Filijala: {data["filijala"]}')
    para.add_run(f'\nDatum važenja zdravstvene knjižice: {data["knjizica"]}\n')
    para.add_run('Ustanova/Referentni Centar: ')
    para.add_run('Klinika za gastroenterohepatologiju UKCS').bold = True

    # 2. Cluster
    #VID TERAPIJE, LEK, REZIM DOZIRANJA
    para = doc.add_paragraph()
    para.add_run('Vid terapije: ')
    para.add_run('1. Uvođenje leka u terapiju  ').bold = (data["vid_terapije"] == 1)
    para.add_run('2. Terapija održavanja  ').bold = (data["vid_terapije"] == 2)
    para.add_run('3. Promena leka   ').bold = (data["vid_terapije"] == 3)
    para.add_run('4. Prekid terapije ').bold = (data["vid_terapije"] == 4)

    para = doc.add_paragraph()
    para.add_run('Lek: ')
    para.add_run('1. Remsima (IFX)  ').bold = (1 in data["lek_lista"])
    para.add_run('2. Inflectra (IFX)  ').bold = (2 in data["lek_lista"])
    para.add_run('3. Humira (ADA)  ').bold = (3 in data["lek_lista"])
    para.add_run('4. Xeljanz (TOFA)  ').bold = (4 in data["lek_lista"])
    para.add_run('5. Entyvio (VDZ)').bold = (5 in data["lek_lista"])

    para = doc.add_paragraph()
    para.add_run('Režim doziranja: ')
    para.add_run('1. STANDARDNI  ').bold = (data["rezim_doziranja"] == 1)
    para.add_run('2. OPTIMIZACIJA').bold = (data["rezim_doziranja"] == 2)


    # 3. Cluster
    para = doc.add_paragraph()
    para.add_run('Pol: ')
    para.add_run('Ž').bold = (data["pol"] != "M")
    para.add_run('/')
    para.add_run('M').bold = (data["pol"] == "M")

    para.add_run('\nGodine života: ')
    para.add_run('\nDg: ')
    dg = para.add_run('Morbus Crohn K50')
    dg.font.bold = True
    dg.font.underline = True

    para.add_run(f'\nTM= {data["tm"]}\t')
    para.add_run(f'TV= {data["tv"]}\t')
    para.add_run(f'BMI= {data["bmi"]}')

 
    # Lokalizacija list
    para = doc.add_paragraph()
    para.add_run('Lokalizacija: ')
    para.add_run('\n1. Ileum').bold = (1 in data["lokalizacija"])
    para.add_run('\n2. Ileum + Kolon').bold = (2 in data["lokalizacija"])
    para.add_run('\n3. Kolon').bold = (3 in data["lokalizacija"])
    para.add_run('\n4. Rektum').bold = (4 in data["lokalizacija"])
    para.add_run('\n5. Proksimalni segmenti GI trakta').bold = (5 in data["lokalizacija"])
    para.add_run('\n6. Drugo').bold = (6 in data["lokalizacija"])

    #TODO - dodaj opciju za DRUGO 



    #Ponasanje bolesti cluster
    para = doc.add_paragraph()
    para.add_run('Ponašanje bolesti: ')
    para.add_run('1. Inflamatorna forma ').bold = (1 in data["ponasanje_bolesti"])
    para.add_run('2. Penetrantna  ').bold = (2 in data["ponasanje_bolesti"])
    para.add_run('3. Stenozantna').bold = (3 in data["ponasanje_bolesti"])


    #Fistula cluster
    para = doc.add_paragraph()
    para.add_run('Fistula/e: ')
    para.add_run('1.Ne ').bold = (len(data["fistula"]) == 0)
    para.add_run('2.Da').bold = (len(data["fistula"]) > 0)
    para.add_run('\n1. Perianalna').bold = (1 in data["fistula"])
    para.add_run('\n2. Enterokutana').bold = (2 in data["fistula"])
    para.add_run('\n3. Enterovaginalna').bold = (3 in data["fistula"])
    para.add_run('\n4. Enteroenteralna').bold = (4 in data["fistula"])
    para.add_run('\n5. Enterovezikalna').bold = (5 in data["fistula"])
    para.add_run('\n6. Drugo').bold = (6 in data["fistula"])

    #TODO - dodaj opciju za DRUGO 


    #Apsces cluster
    para = doc.add_paragraph()
    para.add_run('Apces/-i: ')
    para.add_run('1. Ne ').bold = (len(data["apsces"]) == 0)
    para.add_run('2. Da').bold = (len(data["apsces"]) > 0)
    para.add_run('\n1. Perianalni').bold = (1 in data["apsces"])
    para.add_run('\n2. Interintestinalni').bold = (2 in data["apsces"])
    para.add_run('\n3. Drugo').bold = (3 in data["apsces"])

    #TODO - dodaj opciju za DRUGO


    # 4. Cluster
    #DUZINA TRAJANJA, MANIFESTACIJE, VRSTA EIM
    para = doc.add_paragraph()
    para.add_run(f'Dužina trajanja bolesti: {data["trajanje_bolesti"]}')
    para.add_run('\nEkstraintestinalne manifestacije: ')
    para.add_run('1. Ne ').bold = data["ekstraintestinalne_manifestacije"] == False
    para.add_run('2. Da').bold = data["ekstraintestinalne_manifestacije"] == True
    para.add_run(f'\nVrsta EIM {data["vrsta_eim"]}')


    #Klinicka aktivnost bolesti cluster
    para = doc.add_paragraph()
    para.add_run('Klinička aktivnost bolesti: ')
    para.add_run('1. Blaga ').bold = (data["klinicka_aktivnost"] == 1)
    para.add_run('2. Umerena  ').bold = (data["klinicka_aktivnost"] == 2)
    para.add_run('3. Izrazito aktivna').bold = (data["klinicka_aktivnost"] == 3)
    para.add_run('4. Remisija').bold = (data["klinicka_aktivnost"] == 4)


    # 5. Cluster
    #CRP, FEKALNI KALPROTEKTIN, QUANTIFERON, RTG, CLOSTRIDIUM, HBs
    para = doc.add_paragraph()
    para.add_run(f'Vrednost CRP-a: {data["crp"]}')
    para.add_run(f'\nFekalni kalprotektin: {data["kalprotektin"]}')

    para.add_run('\nQuantiferon gold: ')
    para.add_run('1. Negativan ').bold = data["quantiferon_gold"] == False
    para.add_run('2. Pozitivan').bold = data["quantiferon_gold"] == True

    para.add_run('\nRTG srca i pluća: ')
    para.add_run('1. Nalaz uredan ').bold = data["rtg_uredan"] == True
    para.add_run('2. Izmenjen').bold = data["rtg_uredan"] == False

    para.add_run('\nTest na Clostridium difficile: ')
    para.add_run('1. Negativan ').bold = data["clostridium"] == False
    para.add_run('2. Pozitivan').bold = data["clostridium"] == True

    para.add_run('\nHBs antigen: ')
    para.add_run('1. Negativan ').bold = data["hbs_antigen"] == False
    para.add_run('2. Pozitivan').bold = data["hbs_antigen"] == True



    #6. Cluster
    #ENDOSKOPIJA, OPERACIJA, BR OPERACIJA, RAZLOG OPERACIJE, PRISUTNA
    para = doc.add_paragraph()

    para.add_run('Endoskopija: ')
    para.add_run('1. Prisustvo ulceracija ').bold = data["endoskopija"] == True
    para.add_run('2. Odsustvo ulceracija').bold = data["endoskopija"] == False
    #para.add_run(f'({data["endoskopija"]})').bold = data["endoskopija"] > 0

    para.add_run('\nOperacija: ')
    para.add_run('1. Ne ').bold = data["operacija"] == False
    para.add_run('2. Da').bold = data["operacija"] == True

    para.add_run('\nBroj operacija: ')
    para.add_run('1. Jedna ').bold = data["br_operacija"] == 1
    para.add_run('2. Dve i/ili više').bold = data["br_operacija"] == 2

    para.add_run('\nRazlog operacije: ')
    para.add_run('1. Stenoza ').bold = (1 in data["razlog_operacije"] )
    para.add_run('2. Penetrantna bolest ').bold = (2 in data["razlog_operacije"])
    para.add_run('3. Drugi').bold = (3 in data["razlog_operacije"])
    #TODO dodaj Drugi

    para.add_run('\nPrisutna: ')
    para.add_run('Ileostoma').bold = (1 in data["prisutna"])
    para.add_run('/')
    para.add_run('Kolostoma').bold = (2 in data["prisutna"])


    #DOSADASNJA TERAPIJA
    para = doc.add_paragraph()
    para.add_run('Dosadašnja terapija: ')

    # 1. Kortikosteroidi
    para.add_run('\n1. Korktikosteroidi: ')
    para.add_run('oralno').bold = data["kortiko_oralno"] == True
    para.add_run('/')
    para.add_run('intravenski').bold = data["kortiko_oralno"] == False

    para.add_run(f'\nDoza: {data["kortiko_doza"]}')
    para.add_run(f'\nPočetak terapije: {data["kortiko_pocetak"]}')

    para.add_run('\nKraj terapije').bold = data["kortiko_kraj"] == True
    para.add_run('/')
    para.add_run('Još uvek traje').bold = data["kortiko_kraj"] == False

    para.add_run('\nPoboljšanje nakon trećeg dana ordiniranja: ')
    para.add_run('1. Ne ').bold = data["kortiko_poboljsanje"] == False
    para.add_run('2. Da').bold = data["kortiko_poboljsanje"] == True

    para.add_run('\nKortikozavisan: ')
    para.add_run('1. Ne ').bold = data["kortiko_kortikozavisan"] == False
    para.add_run('2. Da').bold = data["kortiko_kortikozavisan"] == True

    para.add_run('\Kortikorezistentan: ')
    para.add_run('1. Ne ').bold = data["kortiko_kortikorezistentan"] == False
    para.add_run('2. Da').bold = data["kortiko_kortikorezistentan"] == True


    # 2. AZA
    para = doc.add_paragraph()

    para.add_run('2. AZA: ')
    para.add_run(f'\nDoza: {data["aza_doza"]}')
    para.add_run(f'\nPočetak terapije: {data["aza_pocetak"]}')

    para.add_run('\nKraj terapije').bold = data["aza_kraj"] == True
    para.add_run('/')
    para.add_run('Još uvek traje').bold = data["aza_kraj"] == False

    para.add_run('\nAlergija na lek: ')
    para.add_run('1. Ne ').bold = data["aza_alergija"] == False
    para.add_run('2. Da').bold = data["aza_alergija"] == True

    para.add_run('\Rezistentan na imunosupresive: ')
    para.add_run('1. Ne ').bold = data["aza_rezistentan"] == False
    para.add_run('2. Da').bold = data["aza_rezistentan"] == True



    # 3. IFX
    para = doc.add_paragraph()

    para.add_run('2. IFX: ')

    para.add_run(f'\nDoza: {data["ifx_doza"]}')
    para.add_run(f'\nPočetak terapije: {data["ifx_pocetak"]}')
    para.add_run(f'\nBroj ampula po ciklusu: {data["ifx_broj_ampula"]}')
    para.add_run(f'\nPoslednja doza: {data["ifx_poslednja_doza"]}')
    para.add_run(f'\nSledeću dozu treba da primi: {data["ifx_sledeca_doza"]}')
    1
    para.add_run('\nKraj terapije').bold = data["ifx_kraj"] == True
    para.add_run('/')
    para.add_run('Još uvek traje').bold = data["ifx_kraj"] == False


    # Pred kraj
    para = doc.add_paragraph()
    para.add_run('Nuspojave na bilo koje dosadašnje lekove: ')
    para.add_run('1.Ne ').bold = data["nuspojave_na_lekove"] == False
    para.add_run('2.Da').bold = data["nuspojave_na_lekove"] == True

    para.add_run(f'\nLek: {data["nuspojave_lek"]}')
    para.add_run(f'\nVrsta manifestacija: {data["nuspojave_vrsta"]}')
    para.add_run(f'\nUkupno trajanje biološke terapije do sada: {data["trajanje_biloske_terapije"]}')

    # KOMENTAR
    para = doc.add_paragraph()
    dg = para.add_run('KOMENTAR O POTREBI PRIMENE BIOLOŠKE TERAPIJE')
    dg.font.underline = True


    # Kraj
    para = doc.add_paragraph()
    para.add_run(f'Datum: {data["datum"]}')

    para.add_run('\nPotpis članova komisije UKCS: \t\t\t\t Direktor Klinike za GEH:')
    para.add_run('\n\n____________________________ \t\t\t\t ____________________________')
    para.add_run('\n\n____________________________')
    para.add_run('\n\n____________________________')


    #save the document
    doc.save('output.docx')