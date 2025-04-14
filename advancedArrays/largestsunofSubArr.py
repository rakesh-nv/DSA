

arr = [-2,-3,4,-1,-2,1,5,-3]
max = 0
sum=0

for i in range(len(arr)):
    sum = sum+arr[i]
    if sum > max:
        max = sum
    if sum < 0:
        sum = 0

print(max)
    
