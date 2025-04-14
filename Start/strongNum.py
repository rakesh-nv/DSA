# Strong number is factorial of each digit of a number and sum of all the factorials is equal to the number itself.


num = 145

temp = num
fact_sum = 0
while num >0:
    reminder = num % 10
    fact = 1
    for i in range(1, reminder + 1):
        fact = fact * i
    num = num // 10
    fact_sum += fact

if temp == fact_sum:
    print(temp,"It is a Strong number")
else:
    print(temp,"It is not a Strong number")
