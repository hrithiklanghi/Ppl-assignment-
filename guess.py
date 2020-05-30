import random
k=1
j=random.randint(1,100)
while(k==1):
	print("guess the number")
	p=int(input())
	if (p==j):
		print("you got the soulution")
		k=0
	else:
		if(j>p):
			print("number you entered is smaller than ans")
		else:
			print("number you entered is greater than ans")
		

