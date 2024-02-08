list=['abc','xyz','aba','1221','131']
a=0
for i in list:
    if len(i)>=2 and i[0]==i[-1]:
        a+=1
print(a)