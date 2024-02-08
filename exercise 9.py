"""list1=[20,52,34,96,73]
list2=lambda list1:sorted(list1)
answer=list2(list1)
print("Answer:",answer[-3])

list1=["Hi","Good","hello","Bye"]
list2=lambda list1:sorted(list1)
answer=list2(list1)
print("Answer:",answer[-2])"""

def isVowel(ch): 
	return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 

def countVovels(str, n): 
	if (n == 1): 
		return isVowel(str[n - 1]); 

	return (countVovels(str, n - 1) +
				isVowel(str[n - 1])); 
str = "Consonant"; 

print(countVovels(str, len(str))) 
