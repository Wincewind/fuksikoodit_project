class Opiskelija:

    nimi="nimi"
    opintopisteet=0
    suoritetut_kurssit=[]
    kurssit_meneillään=[]
    terveys=100
    motivaatio=100
    stressi=0

    print(nimi)
    print("Suoritat kursseja")
    for kurssi in kurssit_meneillään:
        print(kurssi)

    print("Terveys: " + str(terveys) + "/100")
    print("Motivaatio: " + str(motivaatio) + "/100")
    print("Stressi: " + str(stressi))

    print("Opintopisteitä kasassa: " + str(opintopisteet))
    print("Olet suorittanut kurssit:")
    for kurssi in suoritetut_kurssit:
        print(kurssi)
