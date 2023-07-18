#accept a number to check and print wheter the given number is prime number or not
 
def prime(n):
    if n > 1 :
        #iterate from 2 to n/2
        for i in range(2, int(n/2)+1):
            # if num is divisble by and number in between
            # 2 and n / 2 it is not prime
            if (n % i) == 0:
                print(n,'is not a prime number')
                break
            else:
                 print(n,'is a prime number')
    else:
        print(n,'is not a prime number')
 
print('enter a number')
n=int(input())
print(prime(n))
