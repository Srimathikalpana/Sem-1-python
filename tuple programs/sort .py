def last(n):
	return n[-1] 

def func(tuples):
	return sorted(tuples, key=last)

a=[(1, 3), (3, 2), (2, 1)]
print("Sorted: ",func(a))

