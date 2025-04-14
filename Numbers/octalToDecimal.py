

num = 512
binary_value = num
decimal_value = 0
power = 1

while num >0:
    rem =  num%10
    decimal_value = decimal_value + rem * power
    num = num//10
    power = power * 16

print("Binary Value: ", binary_value)
print("Decimal Value: ", decimal_value)