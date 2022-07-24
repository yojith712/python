print('three digit number')
a=int(input())
firstnumber=a//100
reminder=a%100
print('firstnumber',firstnumber)
print('reminder',reminder)
secondnumber=reminder//10
thirdnumber=reminder%10
reverse=thirdnumber*100+secondnumber*10+firstnumber
print('reverse of three digits',reverse)
