# Python Program to print star pattern using for loop
def pattern(n):
   for i in range(n):
      for j in range(i):
          
        print("*",end="")
         
      print("\r")
n=int(input("enter a number :"))
pattern(n)
