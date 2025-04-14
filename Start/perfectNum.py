

# sum of all divisers of a number is equal to the number itself
# 28 = 1 + 2 + 4 + 7 + 14


n = 28
sum = 0

for i in range(1,n):
    if n% i == 0:
        sum=sum +i

if sum ==n:
    print(n,"It is a perfect number")
else:
    print(n,"It is not a perfect number")