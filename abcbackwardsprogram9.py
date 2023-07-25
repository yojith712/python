# Python Program to print alhabet pattern using for l
def pattern(n):
    alphabet=["A","B","C","D","E","F","G","H","I","J"]
    for i in range(n):
      for j in range(n,-1,-1):
         print(alphabet[j],end="")
      print("\r")
n=int(input("enter a number :"))
pattern(n)
