PÄIVÄ = 1
OPISKELIJA = None
KURSSIT = []
PERIODI = 1

import json
from kurssi import Kurssi
from opiskelija import Opiskelija
import weekController


def alusta_periodi(numero):
    periodin_kurssit = []
    for kurssi in KURSSIT:
        if(kurssi.periodi == PERIODI):
            periodin_kurssit.append(kurssi)

    OPISKELIJA.alusta_periodin_kurssit(periodin_kurssit)


#game tick tässä tapauksessa yksi päivä
def tick():

    #tulosta päivä
    print(f'Tänään on päivä {PÄIVÄ}')

    #tulosta opiskelijan tiedot
    print(OPISKELIJA)

    #tulostaa menossa olevat kurssit
    print(OPISKELIJA.menossaolevien_kurssien_tiedot())

    #tulostaa viikon tapahtumat -milloin palautus - milloin luennot
    weekController.printViiko()

    #Tulostaa käytössä olevat tunnit


    #kysyy ajan allokointia kurssi kerrallaan ja käytökö luennolla
    #Laskee nukkumiseen jäävän ajan ja kysyy kuinka paljon haluaa käyttää

def setup():
    nimi = input('Mikä on nimesi:')
    OPISKELIJA = Opiskelija(nimi)

    with open('kurssit.json') as json_file:
        kurssit = json.load(json_file)
        for kurssi in kurssit:
            KURSSIT.append(Kurssi(kurssi))

#palauttaa unen määrän
def maarita_kursseihin_kautettava_aika(opiskelija,nykyinen_pv):
    paivan_tunnit = 24
    for kurssi in opiskelija.kurssit_meneillään:
        print(f'Määritä kurssin {kurssi.nimi} panos:')
        if nykyinen_pv in kurssi.luennot and paivan_tunnit >= 2:
            while True:
                print('Osallistutko päivän luennolle?')
                valinta = input('Y/N: ')
                if valinta == 'Y' and op:
                    paivan_tunnit -= 2
                    kurssi.kayta_aikaa(2)
                    break
                elif valinta == 'N':
                    break
            
            while True:
                try:
                    harjoituksiin_kaytetty_aika = int(input('Paljon aikaa aiot käyttää tämän viikon palautuksiin? Jäljellä olevaan allokoitavaa aikaa on: {paivan_tunnit}'))
                    if harjoituksiin_kaytetty_aika > paivan_tunnit:
                        pass
                    else:
                        kurssi.kayta_aikaa(harjoituksiin_kaytetty_aika)
                        paivan_tunnit -= harjoituksiin_kaytetty_aika
                except:
                    pass
        return paivan_tunnit


def main():
    print('-'*80)
    print('Opiskelijan seikkailu game 2022')
    print('-'*80)

main()