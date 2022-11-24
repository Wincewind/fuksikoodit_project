import json
import weekController

periodit = 4
periodinkesto = 60

class Palautus:
    def __init__(self):
        self.palautettu = False
        self.pisteet = 0

class Kurssi:
    def __init__(self, json):
        self.nimi = json['nimi']
        self.pisteet = 0
        self.maksimipisteet: json['maksimipisteet']
        self.op = json['op']
        self.palautukset = {}
        self.luennot = []
        self.alkupaiva = -1
        self.loppupaiva = -1
        self.kaytetyt_tunnit = 0
        self.periodi = json['periodi']
        
        viikonpaiva = 0
        paiva = 1

        for periodi in range(1,periodit+1):
            for _ in range(0,periodinkesto):
                if periodi == json['periodi']:
                    if self.alkupaiva == -1:
                        self.alkupaiva = paiva
                    viikonpaivanimi = weekController.viikonpäivät[viikonpaiva]
                    if viikonpaivanimi in json['palautukset']:
                        self.palautukset[paiva] = Palautus()
                    if viikonpaivanimi in json['luennot']:
                        self.luennot.append(paiva)
 
                paiva += 1
                if viikonpaiva < 6:
                    viikonpaiva += 1
                else:
                    viikonpaiva = 0

            if periodi == json['periodi']:
                self.loppupaiva = paiva-1


        self.tentti = 0

        #korvataan viimeinen luento tentillä, jos kurssilla on tentti
        if json['tentti']:
            self.tentti = max(self.palautukset.keys())
            del self.palautukset[self.tentti]

    def get_arvosana(self):
        return 0

    arvosana = property(get_arvosana)


