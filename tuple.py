"""def last(n):
    return n[-1]
def func(tuples):
    return sorted(tuples,key=last)
a=[(1,2),(9,4),(1,3)]
print(func(a))

list1=[(1,2,3,4),(1,1,7,8),(5,8,0)]
k=1
a=[]
for i in list1:
    for j in range(len(i)-1):
        if i[j]==k and i[j+1]==k:
            break
    else:    
        a.append(i)
print(a)        
original_tuple = ()
new_element = 54
ans=8
#for i in range(3):
original_tuple = original_tuple +(ans,new_element)
print(original_tuple)

list1=[(1,2,3),(4,5,6),(7,8,9)]
list3=[]
for i in list1:
    list2=list(i)
    list2[-1]=10
    tuple2=tuple(list2)
    list3.append(tuple2)
print(list3)"""
def last(n):
    return n[0]
dict={1:2,3:4,5:6}
descending=sorted(dict.items(),key=last,reverse=True)
print(descending)
    