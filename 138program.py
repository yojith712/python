#find the value of m power of n value

def power(m,n):
    value=m**n
    return value
 
print('enter a number')    
m=int(input())
print('enter a power of a number')
n=int(input())
print(m,"to the power of",n,"is:",power (m,n))
