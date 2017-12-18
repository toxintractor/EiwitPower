from coordinaatMethode.helpers import *
from coordinaatMethode.monteCarlo import *

def hillClimber(montecarloList):
    print(montecarloList[0].coordinates)
    eiwitstreng = montecarloList[0]
    print (eiwitroute(eiwitstreng))
    print ("Score:", eiwitstreng.score)
    #visualPath(eiwitstreng)


    temperature = 10000
    aantal = 0
    start_time = time.clock()
    while(temperature > 1):
        #temperature = calctemp(temperature)

        aantal += 1
        nieuweroute = routeaanpas(eiwitstreng, eiwitroute(eiwitstreng))
        if finalScore(nieuweroute, eiwitstreng)- counterFirst(eiwitstreng.streng) >= 0:
            eiwitstreng.score += finalScore(nieuweroute, eiwitstreng)- counterFirst(eiwitstreng.streng)
            eiwitstreng.coordinates = nieuweroute
            print("Score:", eiwitstreng.score, "even geduld aub...")
            #print(time.clock() - start_time, "seconds")
            #visualPath(eiwitstreng)
            start_time = time.clock()

        temperature -=  1
    print("Hoogste score:", eiwitstreng.score)
    visualPath(eiwitstreng)

'''
best_score = Monte(1000)

print ('lengte: ', len(best_score))
for i in best_score:
    print (i.score)
    print (i.coordinates)
    print (i.streng)
'''



hillClimber(Monte(500000))