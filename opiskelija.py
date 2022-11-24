class Opiskelija:


    def __init__(self, nimi):
        self.nimi = nimi
        self.opintopisteet = 0
        self.suoritetut_kurssit = []
        self.kurssit_meneillään = []
        self.terveys = 100
        self.motivaatio = 100
        self.stressi = 0

    def __str__(self):
        return f"Terveys: {self.terveys}/100\nMotivaatio: {self.motivaatio}/100\nStressi: {self.stressi}"
        
    def opintopiste_tulostus(self):
        return "Opintopisteitä kasassa: " + str(self.opintopisteet)

    def suoritetut_kurssit_tulostus(self):
        suoritetut=""
        for kurssi in self.suoritetut_kurssit:
            suoritetut+=kurssi+"\n"
        return suoritetut


    def kurssit_meneillään_tulostus(self):
        meneillään=""
        for kurssi in self.kurssit_meneillään:
            meneillään+=kurssi+"\n"
        return meneillään

    def luennot_väliltä(self, alku, loppu):
        luennot={}
        for kurssi in self.kurssit_meneillään:
            for luento in kurssi.luennot:
                if alku<=luento<=loppu:
                    if luento in luennot.keys:
                        luennot[luento].append(kurssi.nimi)
                    else:
                        luennot[luento]=[kurssi.nimi]

                    



    print(nimi)
    print("Suoritat kursseja")
    for kurssi in kurssit_meneillään:
        print(kurssi)

    print("Terveys: " + str(terveys) + "/100")
    print("Motivaatio: " + str(motivaatio) + "/100")
    print("Stressi: " + str(stressi))

    print("Opintopisteitä kasassa: " + str(opintopisteet))
    print("Olet suorittanut kurssit:")
    for kurssi in suoritetut_kurssit:
        print(kurssi)


opiskelija = Opiskelija('matti')
print(opiskelija)
