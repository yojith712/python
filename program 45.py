print(' four  digit ')
a=int(input())
firstnumber=a//1000
reminder=a%1000
print('firstnumber',firstnumber)
print('reminder',reminder)
secondnumber=reminder//100
thirdnumber=reminder%100
fourthnumber=thirdnumber//10
fourthdigit=thirdnumber%10
sum=firstnumber+secondnumber+fourthdigit+fourthnumber
print('sum of the four digits ',sum)
