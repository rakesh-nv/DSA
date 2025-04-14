




def subarr(arr):
    for i in range(len(arr)-1):
        sum =arr[i]
        for j in range(i+1,len(arr)):
            sum =sum+arr[j]
            if sum == 0:
                return True
    return False

arr =[ 4, 2, -3, 1, 6 ]
print(subarr(arr))
            
            


