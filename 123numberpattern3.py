# Python Program to print number pattern using for loop
def pattern(n):
   for i in range(n):
      for j in range(1,n+1):
         print(j,end="")
      print("\r")
n=int(input("enter a number :"))
pattern(n)
