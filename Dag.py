#Alexander den Otter   -   99067410
AlleDagen = ['Maandag','Dinsdag','Woensdag','Donderdag','Vrijdag','Zaterdag','Zondag']
i = 0
print('Alle dagen van de week:\n')
for i in range(0,7):
    print(AlleDagen[i])
    i = i + 1
print('\n')

print('Alle werkdagen:\n')
for i in range(0,5):
    print(AlleDagen[i])
    i = i + 1
print('\n')

print('Alle weekenddagen:\n')
for i in [5, 6]:
    print(AlleDagen[i])
print('\n')

print('Omgekeerde dagen van de week:\n')
for i in reversed(AlleDagen):
    print(i)
print('\n')

print('Omgekeerde werkdagen van de week')
for i in reversed(AlleDagen[0:5]):
    print(i)
print('\n')

print('Omgekeerde weekenddagen van de week')
for i in reversed(AlleDagen[5:7]):
    print(i)

    
