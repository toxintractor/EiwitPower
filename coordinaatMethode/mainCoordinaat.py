from coordinaatMethode.helpers import *
from coordinaatMethode.monteCarlo import *
from coordinaatMethode.helpers import *
from coordinaatMethode.hillClimber import *

if __name__ == '__main__':
    print ("kies de nummer van het algoritme dat je wilt gebruiken:\n"
           "(1) Montecarlo\n"
           "(2) Hillclimbing\n"
           "(3) Simmulated annealing")
    keuze = input()

    if keuze == "1":
        print ("hoeveel Monte Carlo iteraties wil je draaien:")
        iteraties = int(input())
        besteScore = Monte(iteraties)
        for i in besteScore:
            print(i.score)
            print(i.coordinates)
            print(i.streng)
            visualPath(i)
    elif keuze == "2":
        print("hoeveel Monte Carlo iteraties wil je draaien voor je basis streng:")
        iteraties = int(input())
        hillClimber(Monte(iteraties))
    elif keuze == "3":
        print("hoeveel Monte Carlo iteraties wil je draaien voor je basis streng:")
        iteraties = int(input())


