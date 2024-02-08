list=[12,34,56,78,90]
result=[]
for x in list:
    sum=0
    for i in str(x):
        sum+=int(i)
    result.append(sum)
print(result)