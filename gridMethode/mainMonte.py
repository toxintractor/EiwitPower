from monteCarlo import *

if __name__ == '__main__':

	#bepaal de begintijd van het programma
	startTime = time.clock()

	#print het eiwit in arrayvorm
	print (eiwitList())

	# voert het algoritme uit en bewaart de gevonden oplossingen
	result = Monte(1000)

	# print het aantal vouwingen met de hoogste gevonden score
	print ("Aantal Highscore:", len(result))

	x = 0
	for i in result:
		x += 1
		print (x)
		print (i.grid)
		print ("__________________________________________________________________")

	# print de totale runtijd van het programma
	print ("Runtime:", time.clock() - startTime, "seconds")