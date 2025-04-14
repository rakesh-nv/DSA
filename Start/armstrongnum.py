number = 371

num = number

length = len(str(number))
digit = 0
sum = 0

while num > 0:
    digit = num %10
    sum += digit ** length
    num = num //10

if number == sum:
    print("It is an Armstrong number")
else:
    print("It is not an Armstrong number") 
    

