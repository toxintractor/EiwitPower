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

#simanneal(Monte(100000))

'''
i = EiwitStreng(['H0', 'H1', 'P2', 'H3', 'H4', 'H5', 'P6', 'H7'],
                4,
                [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]])

visualPath(i)
'''


#print (time.clock() - start_time, "seconds")
