import random
Kleuren = ['oranje', 'blauw', 'groen', 'bruin']
AantalMNM = 0

def aantalMNM():
    AantalMNM = int(input('Hoeveel MNMs wilt u hebben?'))
    return AantalMNM

def MNMZakVuller(AantalMNM,Kleuren):
    MNMZak = []
    for x in range(AantalMNM):
        RandomNummer = random.randint(0,len(Kleuren) - 1)
        MNMZak.append(Kleuren[RandomNummer])
    return MNMZak

AantalMNM = aantalMNM()
if AantalMNM > 0:
    MNMZak = MNMZakVuller(AantalMNM,Kleuren)
    print(MNMZak)





