PÄIVÄ = 0
OPISKELIJA = None


def ajan_allokointi():
    OPISKELIJA.kurssit


#game tick tässä tapauksessa yksi päivä
def tick():

    #tulosta päivä
    print(f'Tänään on {PÄIVÄ} päivä')

    #tulosta opiskelijan tiedot
    print(OPISKELIJA)

    #tulostaa menossa olevat kurssit
    print(OPISKELIJA.menossaolevien_kurssien_tiedot())

    #tulostaa viikon tapahtumat -milloin palautus - milloin luennot


    #Tulostaa käytössä olevat tunnit
    #kysyy ajan allokointia kurssi kerrallaan ja käytökö luennolla
    #Laskee nukkumiseen jäävän ajan ja kysyy kuinka paljon haluaa käyttää

def setup():
    OPISKELIJA = new Opiskelija()

def main():
    print('-'*80)
    print('Opiskelijan seikkailu game 2022')
    print('-'*80)

main()