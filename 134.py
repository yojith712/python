#print odd numbers from 1 to n(1+3+5+7+....n)
print('enter n value')
n=int(input())
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print('odd sum is ',sum)
