

decimal_num = 21
temp = decimal_num

binary = 0
power = 1

while decimal_num > 0:
    rem = decimal_num % 2
    binary = binary + rem * power
    decimal_num = decimal_num // 2
    power = power * 10

print("Decimal Value: ", temp)
print("Binary Value: ", binary)