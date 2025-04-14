

arr=[5, 2, 3, 4, 1, 6, 7]
sum=7

for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==sum:
            print(arr[i],arr[j])

