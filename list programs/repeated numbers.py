list=[1,2,3,4,1,2,3,4,5,2,4,6,6]
answer=[]
for i in list:
    x=list.count(i)
    if x>1:
        if i not in answer:
            answer.append(i)
print(answer)