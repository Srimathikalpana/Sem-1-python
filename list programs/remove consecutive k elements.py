list=[(1,2,6,6),(4,6,6,5),(1,2,3,4),(5,6,7,8)]
k=6
answer=[]
for tuple in list:
    skip=False
    for i in range(len(tuple)-1):
        if tuple[i]==k and tuple[i+1]==k:
            skip=True
            break
    if skip==False:
        answer.append(tuple)
print(answer)