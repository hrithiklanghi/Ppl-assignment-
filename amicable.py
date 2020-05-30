def fact_sum(num):
	sum1=0
	for i in range(1,(num//2)+1):
			if (num%i==0):
				sum1=sum1+i
	return sum1
count=0

fact_dict = dict()
for x in range (1,100000000):
	if(count==10):
		break
	fact_sum_x = fact_sum(x)
	if fact_sum_x==x:
		continue
	if x==fact_sum(fact_sum_x):
		if x in fact_dict.keys():
			continue
		fact_dict[x]=True
		fact_dict[fact_sum_x] = True
		count+=1
		print(x, fact_sum_x)		



	
