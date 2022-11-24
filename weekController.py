viikonpäivät = ["ma","ti","ke","to","pe","la","su"]

def tulostaViikko(tämä_päivä, opiskelija):
    luennot = opiskelija.luennot_väliltä(tämä_päivä, tämä_päivä+5)
    palautukset = opiskelija.palautukset_väliltä(tämä_päivä, tämä_päivä+5)
    for i, paiva in enumerate(viikonpäivät):
        print(f"{paiva} | Luennot:{luennot[tämä_päivä+i].join(' ')} | Palautukset:{palautukset[tämä_päivä+1].join(' ')}")

def printPäivä(tämä_päivä, opiskelija):
    luennotLista = opiskelija.paivan_palautukset(tämä_päivä)
    luennot = ",".join(luennotLista)
    if len(luennot) > 0:
        print(f"Tänään on kurssien: {luennot} luennot.")
    else:
        print('Tänään ei ole luentoja')

    palautukset = opiskelija.paivan_palautukset(tämä_päivä)
    palautuksetStr = ",".join(palautukset)
    if len(palautukset) > 0:
        print(f"Tänään on kurssien: {palautuksetStr} palautukset.")
    else:
        print('Tänään ei ole palautuksia')
        