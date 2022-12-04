with open('D3\inputday3.txt', 'r') as file:
    data = file.read().split('\n')

import string
values = dict()
for index, letter in enumerate(string.ascii_lowercase):
   values[letter] = index + 1

index = 26
for index, letter in enumerate(string.ascii_uppercase):
   values[letter] = index + 1 +26

prioritet = 0

for line in data:
    compartment1 = line[0:int(((len(line))/2))]
    compartment2 = line[int((((len(line))/2))):int(((len(line))))]
    
    countedlist = []
    for char in compartment1:
        if char in compartment2 and compartment2.find(char) not in countedlist and char not in countedlist:
            prioritet = prioritet + int(values[char])
            countedlist.append(compartment2.find(char))
            countedlist.append(char)
            #Er her det går galt, den teller L to ganger. 

    countedlist.clear()
#Svar del 2
#print(prioritet)

prioritet1 = 0

for i in range(0,len(data)-2,3):
    Sekk1 = data[i]
    Sekk2 = data[i+1]
    Sekk3 = data[i+2]

    for char in Sekk1:
        if char in Sekk2 and char in Sekk3 and char not in countedlist:
            prioritet1 = prioritet1 + int(values[char])
            countedlist.append(char)
    countedlist.clear()
    
print(prioritet1)