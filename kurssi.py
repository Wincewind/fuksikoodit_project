
periodinkesto = 60

class Kurssi:
    def __init__(self, json):
        self.nimi = json.nimi
        self.pisteet = 0
        self.maksimipisteet: json.maksimipisteet
        self.op = json.opintopisteet
        self.luennot = []
        self.tentti = 0

    def get_arvosana():
        return 0
    arvosana = property(get_arvosana)


