
# Harshed number is a number that is divisible by the sum of its digits.
# For example, 21 is a harshed number because 21 is divisible by 2+1=3.
#21%3 != 0 so 21 is not harshed number
num = 21
temp = num

sum = 0

while num > 0:
    rem = num%10
    sum = sum + rem
    num= num //10
    

if sum%temp == 0:
    print(temp,"is harshed number")
else:
    print(temp,"is not harshed number")
