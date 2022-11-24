def tarkista_motivaatio():
    if opiskelija.motivaatio<=10:
        return "Motivaatiosi on vaarallisen vähissä, olet lähellä jättää opintosi kesken"
    if opiskelija.motivaatio<=0:
        return "MOTIVAATIOSI OPINTOIHIN ON KADONNUT, ET OPISKELE ENÄÄ"
        exit()
    if 10<opiskelija.motivaatio<50:
        return "Muista pitää välillä hauskaakin"

    