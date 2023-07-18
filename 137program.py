#write a program to accept a number and print the mathematical table of the givien  number 

def table(n):
    start=1
    stop=21
    txt="{} * {} = {}"
    for i in range (start,stop):
        print(txt.format(n,i,i*n))
        
print('enter a number')
n=int(input())
