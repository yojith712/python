#accept a number t find and print the given number is palindrome or not
 
def reverse(n):
     
     rev=0
     while n>0:
         rev=rev*10+n%10
         n=n//10
     return rev 
n=int(input('enter n value '))
if reverse(n)==n:
    print('palindrome')
else:
    print('not palindrome')
