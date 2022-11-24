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
        self._luennot = {}
        self.alkupaiva = -1
        self.loppupaiva = -1
        self.kaytetyt_tunnit = 0
        self.periodi = json['periodi']
        self._arvosana = 0.0
        
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
                        self.luennot[paiva] = False
 
                paiva += 1
                if viikonpaiva < 6:
                    viikonpaiva += 1
                else:
                    viikonpaiva = 0

            if periodi == json['periodi']:
                self.loppupaiva = paiva-1

        palautuksen_pisteet = self.maksimipisteet/len(self.palautukset)

        for palautus in self.palautukset:
            palautus.pisteet = palautuksen_pisteet

        self.tentti = 0
        self.tentti_tehty = False

        #korvataan viimeinen luento tentillä, jos kurssilla on tentti
        if json['tentti']:
            self.tentti = max(self.palautukset.keys())
            del self.palautukset[self.tentti]

    def get_arvosana(self):
        return int(self._arvosana)

    def kayta_aikaa(self, aika):
        self.kaytetyt_tunnit += aika

    def tee_tentti(self):
        if self.tentti > 0:
            self.tentti_tehty = True

    def lopeta_kurssi(self):
        palautuspisteet_yhteensa = 0
        for palautus in self.palautukset.values():
            palautuspisteet_yhteensa += palautus.pisteet
        palautus_prosentti = palautuspisteet_yhteensa/self.maksimipisteet

        if palautus_prosentti > 0.9:
            self._arvosana = 5
        elif palautus_prosentti > 0.8:
            self._arvosana = 4
        elif palautus_prosentti > 0.7:
            self._arvosana = 3
        elif palautus_prosentti > 0.6:
            self._arvosana = 2
        elif palautus_prosentti > 0.5:
            self._arvosana = 1

        if self.tentti > 0:
            self._arvosana /= 2

        elif self.tentti_tehty:
            osallistutut_luennot = 0
            for luento in self.luennot.values:
                if luento:
                    osallistutut_luennot += 1
            tenttiprosentti = osallistutut_luennot/len(self.luennot)
            if tenttiprosentti > 0.5:
                if tenttiprosentti > 0.9:
                    self._arvosana += 2.5
                elif tenttiprosentti > 0.8:
                    self._arvosana += 2
                elif tenttiprosentti > 0.7:
                    self._arvosana += 1.5
                elif tenttiprosentti > 0.6:
                    self._arvosana += 1
                elif tenttiprosentti > 0.5:
                    self._arvosana += 0.5
                else:
                    self._arvosana = 0
        return self.arvosana



    def palauta(self, paiva):
        palautus = self.palautukset.get(paiva,None)
        if palautus:
            palautus.palautettu = True
            kerroin = self.kaytetyt_tunnit/5
            if kerroin < 1:
                palautus.pisteet *= kerroin
            self.kaytetyt_tunnit = 0

    def osallistu_luennolle(self, paiva):
        if paiva in self.luennot:
            self.luennot[paiva] = True

    def get_luentopaivat(self):
        return self._luennot.keys()

    luennot = property(get_luentopaivat)
    arvosana = property(get_arvosana)


