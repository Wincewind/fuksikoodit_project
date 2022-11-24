from kurssi import Kurssi
# import json

class Opiskelija:


    def __init__(self, nimi):
        self.nimi = nimi
        self.opintopisteet = 0
        self.suoritetut_kurssit = []
        self.kurssit_meneillaan = []
        self.terveys = 100
        self.motivaatio = 100
        self.stressi = 0

    def __str__(self):
        return f"Terveys: {self.terveys}/100\nMotivaatio: {self.motivaatio}/100\nStressi: {self.stressi}"
        
    def opintopiste_tulostus(self):
        return "Opintopisteita kasassa: " + str(self.opintopisteet)

    def suoritetut_kurssit_tulostus(self):
        suoritetut=""
        for kurssi in self.suoritetut_kurssit:
            suoritetut+=kurssi+"\n"
        return suoritetut


    def kurssit_meneillaan_tulostus(self):
        meneillaan="Menenillään olevat kurssit:\n"
        for kurssi in self.kurssit_meneillaan:
            meneillaan+= f"{kurssi.nimi}, tällä viikolla opiskeluun käytetyt tunnit: {kurssi.kaytetyt_tunnit}\n"

        return meneillaan

    def luennot_valilta(self, alku, loppu):
        luennot={}
        for kurssi in self.kurssit_meneillaan:
            for luento in kurssi.luennot:
                if alku<=luento<=loppu:
                    if luento in luennot.keys():
                        luennot[luento].append(kurssi.nimi)
                    else:
                        luennot[luento]=[kurssi.nimi]
        return luennot
                    

    def alusta_periodin_kurssit(self, kurssit: Kurssi):
        self.kurssit_meneillaan = kurssit

    def lopeta_periodi(self):
        for kurssi in self.kurssit_meneillaan:
            kurssi.lopeta_kurssi()
            self.suoritetut_kurssit.append(kurssi)
    
    def paivan_luennot(self, paiva):
        luennot=[]
        for kurssi in self.kurssit_meneillaan:
            for luento in kurssi.luennot:
                if luento==paiva:
                    luennot.append(kurssi.nimi)
                    break
        return luennot

    def paivan_palautukset(self, paiva):
        palautukset=[]
        for kurssi in self.kurssit_meneillaan:
            if paiva in kurssi.palautukset.keys():
                palautukset.append(kurssi.nimi)
        return palautukset

# if __name__=='__main__':
#     with open('kurssit.json') as json_file:
#         periodin_kurssit = json.load(json_file)
#         #kurssi.periodi = "1"
#         for kurssi in periodin_kurssit:
#             periodin_kurssit.append(Kurssi(kurssi))
#     op = Opiskelija('sampo')
#     periodin_kurssit = []
#     for kurssi in []:
#         if(kurssi.periodi == "1"):
#             periodin_kurssit.append(kurssi)

#     op.alusta_periodin_kurssit(periodin_kurssit)
#     op.kurssit_meneillaan_tulostus
