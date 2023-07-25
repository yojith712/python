# Python Program to print number pattern using for loop
def pattern(n):
   for i in range(1,n+1):
      for j in range(n):
         print(i,end="")
      print("\r")
n=int(input("enter a number :"))
pattern(n)
