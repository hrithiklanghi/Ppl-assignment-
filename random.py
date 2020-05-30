
import random
import os
import sys
if __name__ == "__main__": 
	print("Press any key except y to stop the game")
	print
	print("Press y to contiue")

	while 1:
		cond=eval(input())
		os.system('clear')
		if cond=="y":
			print (random.randrange(1,6, 1))
		else:
			os._exit(1)
		
