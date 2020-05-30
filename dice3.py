#python 3.7.1
import random
y = 1
while (y==1):
  print(random.randint(1,7))
  g=input("want to play again(y/n)?")
  if(g=='y'):
    y=1
  else:
    y=0