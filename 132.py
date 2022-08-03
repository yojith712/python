#print natrual numbers numbers from 1 to n(1+2+3+4+....n)
print('enter n value')
n=int(input())
i=1
sum=0
while i<=n:
    sum=sum+i
    i=i+1
print('sum of natrual numbers',sum)
average=sum/n
print('average of given numbers',average)
   
