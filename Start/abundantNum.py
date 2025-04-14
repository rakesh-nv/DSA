
# abundant number is a number for which the sum of its proper divisors is greater than the number itself.
num = 12

sum = 1
for i in range(2,num//2+1):
    if num % i ==0:
        sum = sum+i
        print(sum)


if sum > num:
    print(num,"It is a Abundant number")
else:
    print(num,"It is not a Abundant number")
