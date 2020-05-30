print("enter range of numbers")
k=int(input())
j=int(input())

for i in range(k,j+1):
	sum=0
	temp=i
	while temp>0:
		digit=temp % 10
		sum+=digit**3
		temp=temp//10
	if  i==sum:
		print("the armstrong number is",i)
		
			
