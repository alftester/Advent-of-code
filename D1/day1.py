
with open('D1\inputday1.txt', 'r') as file:
    data = file.read().split('\n')
    
i = 0
elf = [0]

for line in data:
    if len(line)>0:
        elf[int(i)] = elf[int(i)] + int(line)
    elif len(line)==0:
        i = i + 1
        elf.append(int(0)) 

elf.sort(reverse=True)
print("Svar del 1", elf[0])

topp3 = elf[0] + elf[1] + elf[2]
print("svar del 2", topp3)
