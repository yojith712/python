# number pattern 
def pattern(n):
    for i in range(1 ,n+1):
       for j in range(n,0,-1):
           if i >= j: 
               print(j , end =" ")
           else:
                print(" ",end=" ")
       print("")   
n = 5
pattern(n)
