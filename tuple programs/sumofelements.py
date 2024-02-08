list = ((1, 4, 5), (7, 8), (2, 4, 10))
sum = 0
for x in list: 
	for i in x: 
		sum = sum + i
answer= sum/len(x) 
print("The mean of tuple list is : " + str(answer)) 
