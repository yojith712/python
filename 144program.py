#accept a number t find and print the sum of indicidual digits of the given number
 
def getsum(n):
     
     sum=0
     for digit in str(n):
        sum += int(digit)
     return sum
n=12345
print(getsum(n))
