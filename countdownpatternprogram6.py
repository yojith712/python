# Python Program to print number pattern using for l
def pattern(n):
    for i in range(n,0,-1):
      for j in range(n):
         print(i,end="")
      print("\r")
n=int(input("enter a number :"))
pattern(n)
