

arr = [10, 80, 9,56, 4,80,8,90]

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if arr[i] > arr[j]:
            temp = arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        
print(arr)