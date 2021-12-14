import random
mnmZakDictionarybag = {

  "rood" : 0,
  "geel" : 0,
  "bruin" : 0
}

Colors = "rood","geel","bruin"

def begin():
    AantalMNM = int(input('Hoeveel MNMs wilt u hebben?(1-50)\n---> '))
    return AantalMNM

def Kleuren(mnmDictionaryBag,Colors,AantalMNM):
    i = 0
    while i < AantalMNM:
        RandomNumber = random.randint(0,len(Colors) - 1)
        Color = Colors[RandomNumber]
        mnmDictionaryBag[Color] += 1
        i = i + 1
    return mnmZakDictionarybag,Colors

        
    

def MoetMeerDan0():
    if mnmZakDictionarybag["rood"] == 0:
        del mnmZakDictionarybag["rood"]
    if mnmZakDictionarybag["geel"] == 0:
        del mnmZakDictionarybag["geel"]
    if mnmZakDictionarybag["bruin"] == 0:
        del mnmZakDictionarybag["bruin"]

def SorteerMNMZak():
    GesorteerdeZak = sorted(mnmZakDictionarybag.items(), key=lambda x: x[1])
    return GesorteerdeZak

def ZakMetMNM_Einde(GesorteerdeZak):
    print('\nU heeft dus een zak met:')
    print(str(GesorteerdeZak)+ " MNM's\n")

AantalMNM = begin()

if AantalMNM >= 1 and AantalMNM <= 50:
    Kleuren(mnmZakDictionarybag,Colors,AantalMNM)
MoetMeerDan0()
GesorteerdeZak = SorteerMNMZak()
ZakMetMNM_Einde(GesorteerdeZak)



