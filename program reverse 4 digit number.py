print('fourth  digit number')
a=int(input())
firstnumber=a//1000
reminder=a%1000
print('firstnumber',firstnumber)
print('reminder',reminder)
secondnumber=reminder//100
thirdnumber=reminder%100
print('thirdnumber',thirdnumber)
fourthnumber=thirdnumber//10
fourthdigit=thirdnumber%10
print('fourthdigit',fourthdigit)
reverse=fourthdigit*1000+fourthnumber*100+secondnumber*10+firstnumber
print('reverse of four digit',reverse)
