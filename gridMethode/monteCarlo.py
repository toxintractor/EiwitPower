from helpers import *

def Monte(iteraties):
    
    # maakt een list voor de mogelijke directions
    directions = ["l", "r", "u", "d"]
    
    # counter voor het aantal geprobeerde moves
    counter = 0

    # maakt de grid aan de hand van het eiwit
    gridStart = makeGrid(eiwitList())

    # zet het beginpunt op het midden van de grid en plaatst het tweede aminozuur rechts 
    # van het eerste aminozuur om de rotatie-symmetrische oplossingen te prunen
    punt = ((len(eiwitList()) - 1), (len(eiwitList()) - 1))
    punt = moveAmino(punt, "r")
    gridStart[punt[0]][punt[1]] = eiwitList()[1]

    # houdt de best gevonden score bij van de gevonden eiwit vouwingen en voegt deze vouwing 
    # toe aan de lijst van best gevonden scores
    highScore = 0
    highScoreList = []

    # voert het Monte Carlo algoritme n keer uit
    for i in range(iteraties):

        # zet de gridstart om in een numpy grid en reset het punt op het beginpunt (=het tweede aminozuur)
        gridResult = np.copy(gridStart)
        puntStart = ((len(eiwitList()) - 1), (len(eiwitList())))

        # loop die het eiwit vouwingen laat doorlopen
        for i in eiwitList()[2:]:

            # onthoudt een niet toegestane move voor het huidige aminozuur
            forbidDirection = []

            while True:

                counter += 1

                # selecteert de locatie van het huidige aminozuur
                punt = puntStart

                # kiest een random direction en voert een move uit
                direction = (randint(0, 3))
                punt = moveAmino(punt, directions[direction])

                # break als deze move is toegestaan
                if gridResult[punt[0]][punt[1]] == '_':
                    break

                # onthoudt de niet toegestane moves    
                forbidDirection.append(directions[direction])

                # break als alle moves niet zijn toegestaan
                if len(forbidDirection) > 4:
                    break
            
            # plaatst het huidige aminozuur op de grid en verzet het punt
            gridResult[punt[0]][punt[1]] = i
            puntStart = punt

        # als de eindscore beter is dan de huidige beste score
        if endScore(gridResult) < highScore:

            # maak van deze eindscore de nieuwe beste score
            highScore = endScore(gridResult)

            # leeg de lijst van de voorgaande best gevonden vouwingen
            highScoreList = []

            # en voeg de nieuwe beste vouwing toe aan de lijst van best gevonden vouwingen
            highScoreList.append(EiwitStreng(gridResult, highScore))

        # als de eindscore net zo goed is als de huidige beste score
        if endScore(gridResult) == highScore:

            # voeg de nieuwe beste vouwing toe aan de lijst van best gevonden vouwingen
            highScoreList.append(EiwitStreng(gridResult, highScore))

    print ("Aantal uitgevoerde MonteCarlo:", iteraties)
    print ("Aantal geprobeerde moves:", counter)

    # return de best gevonden vouwingen
    return highScoreList
