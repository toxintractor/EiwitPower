from coordinaatMethode.helpers import *

def Monte(n):
    directions = ["l", "r", "u", "d"]
    highScore = 0
    highScoreList = []
    protein = EiwitStreng(inputToList(), counterFirst(inputToList()), [])
    coordinateStart = protein.coordinates[:]
    print (protein.streng)
    print("Basis streng wordt berekend, even geduld aub...")
    print ("------------------------------------------------")

    for i in range(n):
        coordinates = protein.coordinates[:]
        # print 'startcoordinaten:', coordinateStart
        puntStart = protein.pointStart[:]
        for i in range(len(protein.streng[2:])):
            # print i
            # print puntStart
            forbidDirection = []

            punt = puntStart
            direction = (randint(0, 3))
            punt = moveAmino(punt, directions[direction])
            # print punt

            while True:
                punt = puntStart
                direction = (randint(0, 3))
                punt = moveAmino(punt, directions[direction])
                # print directions[direction]
                if ([punt[0], punt[1]]) not in coordinates:
                    # print gridResult
                    break
                if directions[direction] not in forbidDirection:
                    forbidDirection.append(directions[direction])
                if len(forbidDirection) == 4:
                    break
            #print coordinates
            if len(forbidDirection) != 4:
                coordinates[i + 2] = [punt[0], punt[1]]
                puntStart = punt

        # print coordinates
        # print 'score:', finalScore(coordinates, protein)

        if len(forbidDirection) != 4:
            if finalScore(coordinates, protein) > highScore:
                highScore = finalScore(coordinates, protein)
                highScoreList = []
                highScoreList.append(EiwitStreng(protein.streng[:], highScore, coordinates))
            if finalScore(coordinates, protein) == highScore:
                highScoreList.append(EiwitStreng(protein.streng[:], highScore, coordinates))

                # print gridResult
                # counter +=1
                # print counter
    return highScoreList

best_score = Monte(100000)

print ('lengte: ', len(best_score))

for i in best_score:
    print (i.score)
    print (i.coordinates)
    print (i.streng)
    visualPath(i)

print (time.clock() - start_time, "seconds")
