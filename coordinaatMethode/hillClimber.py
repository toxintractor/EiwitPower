from helpers import *
from monteCarlo import *

def simanneal(eiwitstreng):
    eiwitstreng = eiwitstreng
    print (eiwitroute(eiwitstreng))
    #visualPath(eiwitstreng)


    temperature = 1000
    aantal = 0
    start_time = time.clock()
    while(temperature > 1):
        #temperature = calctemp(temperature)

        aantal += 1
        nieuweroute = routeaanpas(eiwitstreng, eiwitroute(eiwitstreng))
        if finalScore(nieuweroute, eiwitstreng)- counterFirst(eiwitstreng.streng) >= 0:
            eiwitstreng.score += finalScore(nieuweroute, eiwitstreng)- counterFirst(eiwitstreng.streng)
            eiwitstreng.coordinates = nieuweroute
            #print (eiwitstreng.score)
            #print(time.clock() - start_time, "seconds")
            #visualPath(eiwitstreng)
            start_time = time.clock()

        temperature -=  1
    visualPath(eiwitstreng)
    print (eiwitstreng.score)
    print (aantal)

best_score = Monte(10)

print ('lengte: ', len(best_score))
for i in best_score:
    print (i.score)
    print (i.coordinates)
    print (i.streng)



simanneal(i)