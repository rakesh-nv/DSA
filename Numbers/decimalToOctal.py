
decimal = 148
decimal_value = decimal
power = 1
octal = 0

while decimal > 0:
    rem = decimal % 8
    octal = octal + rem * power
    decimal = decimal // 8
    power = power * 10

print("Decimal Value: ", decimal_value)
print("Octal Value: ", octal)
