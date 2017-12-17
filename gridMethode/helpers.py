import numpy as np
from itertools import product
import time
from random import randint

class EiwitStreng:
    def __init__(self, grid, score):
        self.grid = grid
        self.score = score

# functie zet een eiwit om in een array met aminozuren en index
def eiwitList():

    index = 0
    eiwit = []
    
    # eiwitInput bevat de eiwitstreng
    eiwitInput = "HHPHHHPH"

    # voegt aan elk aminozuur een index toe en zet het in de eiwit array
    for i in eiwitInput.upper():
        if i != 'H' and i != 'P':
            print ("Het eiwit mag geen", i, "bevatten")
            return "Het eiwit mag geen", i, "bevatten"
        eiwit.append(i + str(index))
        index +=1

    return eiwit

# functie stelt een beginscore op voor opeenvolgende H's in de streng
def startScore():
    score = 0

    for i in range(len(eiwitList()) - 1):
        if eiwitList()[i][0] == "H" and eiwitList()[i+1][0] == "H":
            score += 1

    return score

# functie maakt een Grid-Array aan de hand van de ingevoerde eiwit
def makeGrid(eiwit):

    # de grid krijgt 2 maal de lengte van het eiwit - 1 en plaatst het eerste aminozuur in
    # het midden van de grid
    grid = [["_"] * ((len(eiwit) * 2) - 1) for i in (range(len(eiwit * 2) - 1))]
    grid[len(eiwitList()) - 1][len(eiwitList()) - 1] = eiwit[0]

    # de grid wordt omgezet in een numpy array
    grid = np.array(grid, dtype = '|U16')

    return grid

# functie plaats een nieuw aminozuur in de grid adhv de opgegeven richting
def moveAmino(point, direction):

    # maakt een variabele aan voor het punt van het nieuwe aminozuur
    newPoint = (0,0)

    # plaatst het nieuwe aminozuur
    if direction == "l":
        newPoint = (point[0], point[1] - 1)
    elif direction == "r":
        newPoint = (point[0], point[1] + 1)
    elif direction == "u":
        newPoint = (point[0] - 1, point[1])
    elif direction == "d":
        newPoint = (point[0] + 1, point[1])

    return newPoint

# functie bepaald de eindscore van de vouwing van het eiwit
def endScore(grid):

    score = 0

    # checkt voor elk punt op de grid of het een H bevat, en of het punt rechts of onder dit punt
    # ook een H bevat om dit toe te voegen aan de totale score
    for j in range(len(grid) - 1):
        for k in range(len(grid[j]) - 1):

            if grid[j][k] != '_' and grid[j][k][0] == 'H':
                if grid[j+1][k] != '_' and grid[j+1][k][0] == 'H':
                    score += 1
                if grid[j][k+1] != '_' and grid[j][k+1][0] == 'H':
                    score += 1

    # berekent de totale score door de eindscore van de beginscore af te trekken
    totalScore = startScore() - score 

    return totalScore