import time
from random import randint

import networkx as nx
import pylab as plt

start_time = time.clock()

class EiwitStreng:
    def __init__(self, streng, score, coordinates):
        self.streng = streng
        self.score = score
        self.coordinates = coordinates
        if self.coordinates == []:
            self.coordinates = self.eiwitCoordinates()
        self.pointStart = (self.coordinates[1][0], self.coordinates[1][1])

    def eiwitCoordinates(self):
        self.coordinates = [['_', '_'] for i in self.streng[2:]]
        self.coordinates = [[len(self.streng), len(self.streng)],
                            [len(self.streng) + 1, len(self.streng)]] + self.coordinates

        return self.coordinates

#Functie om het pad te visualiseren.
def visualPath(protein):


    G = nx.Graph()
    colors = []
    for i in range(len(protein.streng)):
        if protein.streng[i][0] == "H":
            G.add_node(protein.streng[i], pos = (protein.coordinates[i][0], protein.coordinates[i][1]))
            colors.append('r')
        if protein.streng[i][0] == "P":
            G.add_node(protein.streng[i], pos = (protein.coordinates[i][0], protein.coordinates[i][1]))
            colors.append('b')
        if protein.streng[i][0] == "C":
            G.add_node(protein.streng[i], pos = (protein.coordinates[i][0], protein.coordinates[i][1]))
            colors.append('y')
    G.add_path(protein.streng)
    '''
    for i in range(len(proteinString)):
        xas, yas = np.where(grid == proteinString[i])
        G.add_node(proteinString[i], pos=(xas[0], yas[0]))
    G.add_path(proteinString)
    '''

    nx.draw_networkx(G, nx.get_node_attributes(G, 'pos'), node_color= colors, with_labels=True)
    plt.show()

# Functie vraagt input aan en zet het om in een array met index.
def inputToList():
    n = 0;
    pt = []
    # eiwitInput = raw_input("voer de eiwit in: ")
    #eiwitInput = "hhphhhph"
    eiwitInput = "CPPCHPPCHPPCPPHHHHHHCCPCHPPCPCHPPHPC"
    #eiwitInput = "PPPHHPPHHPPPPPHHHHHHHPPHHPPPPHHPPHPP"
    #eiwitInput = "PPHPPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
    #eiwitInput = "HHPHPHPHPHHHHPHPPPHPPPHPPPPHPPPHPPPHPHHHHPHPHPHPHH"
    for i in eiwitInput.upper():
        if i != "H" and i != "P" and i != "C":
            print ("Het eiwit mag geen", i, "bevatten")
            return "Het eiwit mag geen", i, "bevatten"
        pt.append(i + str(n))
        n += 1

    #eiwit = EiwitStreng(pt, counterFirst(pt), [])

    return pt

    return eiwit


# Deze functie heeft een +1 score voor elke H's die naast elkaar staan.
def counterFirst(indexList):
    counter = 0
    for i in range(len(indexList) - 1):
        if indexList[i][0] == "H" and indexList[i + 1][0] == "H":
            counter += 1
        elif indexList[i][0] == "H" and indexList[i + 1][0] == "C":
            counter += 1
        elif indexList[i][0] == "C" and indexList[i + 1][0] == "H":
            counter += 1
        elif indexList[i][0] == "C" and indexList[i + 1][0] == "C":
            counter += 5
    return counter


# Deze functie plaats een nieuwe aminozuur in de grid adh van opgegeven richting
def moveAmino(point, direction):
    newPoint = (0, 0)
    '''
    if direction == "l":
        newPoint = (point[0], point[1] - 1)
    elif direction == "r":
        newPoint = (point[0], point[1] + 1)
    elif direction == "u":
        newPoint = (point[0] - 1, point[1])
    elif direction == "d":
        newPoint = (point[0] + 1, point[1])
    '''
    if direction == "l":
        newPoint = (point[0] -1, point[1])
    elif direction == "r":
        newPoint = (point[0]+1, point[1])
    elif direction == "u":
        newPoint = (point[0], point[1]-1)
    elif direction == "d":
        newPoint = (point[0], point[1]+1)

    return newPoint


def finalScore(coordinateList, protein):
    score = 0
    for i in range(len(coordinateList)):
        if ([coordinateList[i][0], coordinateList[i][1] + 1]) in coordinateList:
            j = coordinateList.index([coordinateList[i][0], coordinateList[i][1] + 1])
            if protein.streng[i][0] == 'H' and protein.streng[j][0] == 'H':
                score += 1
            elif protein.streng[i][0] == 'H' and protein.streng[j][0] == 'C':
                score += 1
            elif protein.streng[i][0] == 'C' and protein.streng[j][0] == 'H':
                score += 1
            elif protein.streng[i][0] == 'C' and protein.streng[j][0] == 'C':
                score += 5
        if ([coordinateList[i][0] + 1, coordinateList[i][1]]) in coordinateList:
            j = coordinateList.index([coordinateList[i][0] + 1, coordinateList[i][1]])
            if protein.streng[i][0] == 'H' and protein.streng[j][0] == 'H':
                score += 1
            elif protein.streng[i][0] == 'H' and protein.streng[j][0] == 'C':
                score += 1
            elif protein.streng[i][0] == 'C' and protein.streng[j][0] == 'H':
                score += 1
            elif protein.streng[i][0] == 'C' and protein.streng[j][0] == 'C':
                score += 5
                # print i[j]

    #print ('beginscore =',protein.score)
    return score - protein.score

def routeaanpas(eiwitstreng, route):
    directions = ["l", "r", "u", "d"]
    while True:
        checkdubbel = False
        coordinaten = eiwitstreng.coordinates[:]
        while True:
            randomrichting1 = directions[randint(0,3)]
            randompositie1 = randint(1, len(route)-1)
            randomrichting2 = directions[randint(0, 3)]
            randompositie2 = randint(1, len(route) - 1)
            if randompositie1!= randompositie2 and route[randompositie1] != randomrichting1 and route[randompositie2] != randomrichting2:
                break
        route[randompositie1] = randomrichting1
        route[randompositie2] = randomrichting2

        if randompositie1 < randompositie2:
            startpositie = randompositie1
        else:
            startpositie = randompositie2

        for i in range(startpositie, len(route)):
            verplaatsing  = moveAmino(coordinaten[i],route[i])
            if ([verplaatsing[0], verplaatsing[1]]) in coordinaten[:i+1]:
                checkdubbel = True
                break
            coordinaten[i+1] = [verplaatsing[0], verplaatsing[1]]
        if checkdubbel == False:
            break
    return coordinaten

def eiwitroute(eiwitstreng):
    #print (eiwitstreng.coordinates)
    #directions = [0 for i in range(len(eiwitstreng.coordinates[2:]))]
    directions = ['r']
    #print (len(directions))
    #print (directions)

    for i in range(len(eiwitstreng.coordinates[:-2])):
        x = eiwitstreng.coordinates[i+2][0] - eiwitstreng.coordinates[i+1][0]
        y = eiwitstreng.coordinates[i+2][1] - eiwitstreng.coordinates[i+1][1]
        if  x == 1 and y ==0:
            directions.append('r')
        elif  x == -1 and y ==0:
            directions.append('l')
        elif  x == 0 and y == -1:
            directions.append('u')
        elif  x == 0 and y == 1:
            directions.append('d')

    return directions