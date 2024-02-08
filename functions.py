"""def simple_interest(p,n,age):
    if age>=60:
        si=(p*n*12)/100
        return si
    else:
        si=(p*n*10)/100
        return si
p=int(input("Enter the principal amount:"))
n=int(input("Enter the number of years:"))
age=int(input("Enter the age of the person:"))
interest=simple_interest(p,n,age)
print(interest)

def volume(l,w,h):
    vol=l*w*h
    return vol
volume=volume(12,32,5)
print(volume)"""

def sum_of_series(n):
    return sum([i**2 for i in range(1, n+1)])

n = int(input("Enter a positive integer: "))
print(f"The sum of the series 1^2 + 2^2 + ... + {n}^2 is {sum_of_series(n)}.")
