import random
spelList = ['Monopoly', 'Yathzee', 'Bridge', 'Poker', 'Pesten', 'Mens erger je niet', 'Cluedo']
minimum = [3,4,5,6,7,8,9,10]
maximum = [3,4,5,6,7,8,9,10]

def spelProgramma(spelList,minimum,maximum):
    while maximum == minimum or maximum <= minimum:
        minimum = int(input('Kies het minimum aantal spellen. 3-10\n--->'))
        maximum = int(input('Kies het maximaal aantal spellen. 3-10\n--->'))
        RandomAantalSpellen = random.randint(minimum,maximum)
    for i in range(RandomAantalSpellen):
        RandomGetal = random.randint(0,7)
        print(spelList[RandomGetal])

spelProgramma(spelList,minimum,maximum)

