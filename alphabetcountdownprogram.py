# Python Program to print ALPHABET pattern using for l
def pattern(n):
    alphabet=["A","B","C","D","E","F","G","H","I","J"]
    for i in range(n,-1,-1):
      for j in range(n):
         print(alphabet[i],end="")
      print("\r")
n=int(input("enter a number :"))
pattern(n)
