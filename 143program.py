#accept a number to check and print the given number is a perfect number or not

def isperfect( n ):
    
    # to store sum of divisors
    sum = 1 
    
    #find all divisors and add them
    i=2
    while i * i <=n:
        if n % i == 0:
            sum = sum + i + n/i
        i+=1 
        
     # If sum of divisors is equal to
    # n, then n is a perfect number
    
    return(True if sum == n and n!=1 else False)
    
print("Below are all perfect numbers till 10000")
n = 2
for n in range (10000):
    if isperfect (n):
        print(n , " is a perfect number")
