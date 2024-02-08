list1=[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
answer1=[]
for tuples in list1:
    list2=list(tuples)
    list2[-1]=100
    answer=tuple(list2)
    answer1.append(answer)
print(answer1)