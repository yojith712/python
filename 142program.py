def print_factors(x):

   value=0 
   for i in range(1, x + 1):
       if x % i == 0:
         value=value+i
   print (value)

num = 5

print_factors(num)
