from kurssi import Kurssi


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
                    if luento in luennot.keys():
                        luennot[luento].append(kurssi.nimi)
                    else:
                        luennot[luento]=[kurssi.nimi]
        return luennot
                    

    def alusta_periodin_kurssit(self, kurssit: Kurssi):
        self.kurssit_meneillään = kurssit

    def lopeta_periodi(self):
        for kurssi in self.kurssit_meneillään:
            kurssi.lopeta_kurssi()
            self.suoritetut_kurssit.append(kurssi)
    
    def päivän_luennot(self, päivä):
        luennot=[]
        for kurssi in self.kurssit_meneillään:
            for luento in kurssi.luennot:
                if luento==päivä:
                    luennot.append(luento)
        return luennot

    def päivän_palautukset(self, päivä):
        palautukset=[]
        for kurssi in self.kurssit_meneillään:
            if päivä in kurssi.palautukset.keys():
                palautukset.append(kurssi.palautukset[päivä])
        return palautukset

