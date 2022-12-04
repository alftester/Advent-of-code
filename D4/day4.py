with open('D4\inputday4.txt', 'r') as file:
    data = file.read().split('\n')

par = []
teller = 0
tallrekke = []

for line in data:
    par.append(line.replace('-', ','))

for pos in par:
    tallrekke.append(pos.split(','))
# Ble litt rotete kode her...

for linje in tallrekke:
    # Finner hvilken som har størst spenn
    linje = [eval(i) for i in linje]
    # Hvis den til venstre er størst
    if linje[1]-linje[0] >= linje[3]-linje[2]:
        if linje[0] <= linje[2] and linje[1] >= linje[3]:
            teller = teller + 1

    # hvis rekka til høyre er størst
    elif linje[1]-linje[0] <= linje[3]-linje[2]:
        if linje[2] <= linje[0] and linje[3] >= linje[1]:
            teller = teller + 1

#Svar del 1
#print(teller)

teller1 = 0

for linje in tallrekke:
    # Finner hvilken som har størst spenn
    linje = [eval(i) for i in linje]

    # Hvis den til venstre er størst
    if linje[0] >= linje[2] and linje[0] <= linje[3]:
        teller1 = teller1 + 1

     # Hvis den til høyre er størst
    elif linje[2] >= linje[0] and linje[2] <= linje[1]:
        teller1 = teller1 + 1

print(teller1)