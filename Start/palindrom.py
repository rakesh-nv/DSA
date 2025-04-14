

num = 1221
temp = num
reverse = 0

while num > 0:
    rem = num%10
    reverse = (reverse * 10) + rem
    num = num // 10

if temp == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")