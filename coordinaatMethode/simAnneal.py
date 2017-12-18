import math
from mpmath import rand, exp

from coordinaatMethode.helpers import *
from coordinaatMethode.monteCarlo import *
from copy import deepcopy

def simanneal(montecarloList):
    print(montecarloList[0].coordinates)
    eiwitstreng = montecarloList[0]
    print (eiwitroute(eiwitstreng))
    #visualPath(eiwitstreng)


    temperature = 5
    aantal = 0
    start_time = time.clock()
    highscorestreng = eiwitstreng.coordinates[:]
    highscorescore = deepcopy(eiwitstreng.score)



    while(temperature > 1):
        #temperature = calctemp(temperature)

        nieuweroute = routeaanpas(eiwitstreng, eiwitroute(eiwitstreng))
        scoredifference = finalScore(nieuweroute, eiwitstreng) - counterFirst(eiwitstreng.streng)

        if scoredifference >= 0:
            print ("de score in score:", eiwitstreng.score + scoredifference)
            eiwitstreng.score += scoredifference
            eiwitstreng.coordinates = nieuweroute
            #print (eiwitstreng.score)
            #print(time.clock() - start_time, "seconds")
            #visualPath(eiwitstreng)
            start_time = time.clock()
            print(temperature)

            if eiwitstreng.score > highscorescore:
                highscorestreng = eiwitstreng.coordinates[:]
                highscorescore = deepcopy(eiwitstreng.score)

        elif scoredifference < 0 and (-scoredifference/temperature) < rand():
            eiwitstreng.score += scoredifference
            eiwitstreng.coordinates = nieuweroute
            print(scoredifference)
            print("de scoredifference:", math.exp(scoredifference/temperature), ',', rand())
        aantal += 1

        temperature *=  0.99995
    eiwitstreng.coordinates = highscorestreng
    eiwitstreng.score = highscorescore
    print(eiwitstreng.score)
    print (aantal)
    visualPath(eiwitstreng)
    print (highscorescore)
'''
best_score = Monte(1000)

print ('lengte: ', len(best_score))
for i in best_score:
    print (i.score)
    print (i.coordinates)
    print (i.streng)
    visualPath(i)
'''

simanneal(Monte(1000))

'''
i = EiwitStreng(['P0', 'P1', 'P2', 'H3', 'H4', 'P5', 'P6', 'H7', 'H8', 'P9', 'P10', 'P11', 'P12', 'P13', 'H14', 'H15', 'H16', 'H17', 'H18', 'H19', 'H20', 'P21', 'P22', 'H23', 'H24', 'P25', 'P26', 'P27', 'P28', 'H29', 'H30', 'P31', 'P32', 'H33', 'P34', 'P35'],
                4,
                [[36, 36], [37, 36], [37, 35], [37, 34], [37, 33], [38, 33], [38, 32], [38, 31], [39, 31], [39, 32],
                 [39, 33], [40, 33], [40, 32], [40, 31], [40, 30], [39, 30], [38, 30], [37, 30], [36, 30], [36, 31],
                 [37, 31], [37, 32], [36, 32], [35, 32], [34, 32], [34, 33], [34, 34], [33, 34], [32, 34], [32, 35],
                 [33, 35], [34, 35], [34, 36], [34, 37], [33, 37], [33, 36]])
simanneal(i)
'''



print (time.clock() - start_time, "seconds")
