class Tapahtuma:
    def __init__(self,json: object) -> None:
        self.kuvaus = json['kuvaus']
        self.vaihtoehdot = json['vaihtoehdot']
        self.kesto = json['kesto']

