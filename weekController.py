viikonpäivät = ["ma","ti","ke","to","pe","la","su"]

def tulostaViikko(self, tämä_päivä, opiskelija):
    luennot = opiskelija.luennot_väliltä(tämä_päivä, tämä_päivä+5)
    palautukset = opiskelija.palautukset_väliltä(tämä_päivä, tämä_päivä+5)
    for i, paiva in enumerate(viikonpäivät):
        print(f"{paiva} | Luennot:{luennot[tämä_päivä+i].join(' ')} | Palautukset:{palautukset[tämä_päivä+1].join(' ')}")

    