with open('D2\inputday2.txt', 'r') as file:
    data = file.read().split('\n')

score = 0

for line in data:
    #Rock #Motstander
    if line[0] == "A":
        #Rock #meg
        if line[2] == "X": #Draw
            score = score + 1 + 3
        #Paper #meg
        elif line[2] == "Y": #Win
            score = score + 2 + 6
        #Scissors #meg
        elif line[2] == "Z": #Loss
            score = score + 3 + 0
    
    #Paper #motstander
    elif line[0] == "B":
        #Rock #meg
        if line[2] == "X": #Loss
            score = score + 1 + 0
        #Paper #meg
        elif line[2] == "Y": #Draw
            score = score + 2 + 3
        #Scissors #meg
        elif line[2] == "Z": #Win
            score = score + 3 + 6

    #Scissors #motstander
    elif line[0] == "C":
        #Rock #meg
        if line[2] == "X": #Win
            score = score + 1 + 6
        #Paper #meg
        elif line[2] == "Y": #Loss
            score = score + 2 + 0
        #Scissors #meg
        elif line[2] == "Z": #Draw
            score = score + 3 + 3

print(score)

#Del 2
score = 0


for line in data:
    #Rock #Motstander
    if line[0] == "A":
        if line[2] == "X": #Loss #saks
            score = score + 3 + 0
        elif line[2] == "Y": #draw #Rock
            score = score + 1 + 3
        elif line[2] == "Z": #Win #Paper
            score = score + 2 + 6
    
    #Paper #motstander
    elif line[0] == "B":
        if line[2] == "X": #Loss #Rock
            score = score + 1 + 0
        elif line[2] == "Y": #Draw #Paper
            score = score + 2 + 3
        elif line[2] == "Z": #Win #Saks
            score = score + 3 + 6

    #Scissors #motstander
    elif line[0] == "C":
        if line[2] == "X": #Loose #Paper
            score = score + 2 + 0
        elif line[2] == "Y": #Draw #Saks
            score = score + 3 + 3
        elif line[2] == "Z": #Win #Rock
            score = score + 1 + 6

print(score)