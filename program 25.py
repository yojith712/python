print('four digit number')
input=int(input())
firstnumber=input//1000
secondnumber=input%1000
seconddigit=secondnumber//100
reminder=secondnumber%100
thirddigit=reminder//10
fourthdigit=reminder%10
sum=firstnumber+seconddigit+thirddigit+fourthdigit
print('sum',sum)

