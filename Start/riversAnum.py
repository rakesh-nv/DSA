# riverse a number using recurshan



num = 1234
temp = num
riverse = 0

while num > 0:
    reminder = num % 10
    riverse = (riverse * 10) + reminder
    num = num // 10

print(riverse)
