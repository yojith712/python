#accept a number to count and print the factors of given number

def factors(n):
    count = 0
    print('the factors are')
    for i in range(1, n + 1):
       if n % i == 0:
           count = count +1
           print(i)
    return count

print('enter a number')
n=int(input())
print("The count of factors of ",n,"is:",factors(n))
