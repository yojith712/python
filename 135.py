#print multiplaction numbers from 1 to n(2+4+6+8+10+....+n)
print('enter n value')
n=int(input())
i=2
factorial=1
while i<=n:
    factorial=factorial*i
    i=i+1
print('factoral of n is ',factorial)

