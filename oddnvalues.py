#find and print the sum of 1 to n odd numbers
print('enter a number')
n=int(input())
i=1 
sum=0
while  i <= n:
    if i % 2 != 0:
        sum=sum+i
    i = i + 1
print(sum )
