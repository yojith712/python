#print even numbers from 1 to n(2+4+6+8+10+....+n)
print('enter n value')
n=int(input())
i=2
sum=0
while i<=n:
    sum=sum+i
    i=i+2
print('even sum is ',sum)

