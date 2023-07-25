# Python Program to print star pattern using for loop
def pattern(n):
   for i in range(n):
      for j in range(n):
         print("*",end="")
      print("\r")
n=int(input("enter the number of rows:"))
pattern(n)
