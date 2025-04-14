


import sys

def sumOfMinAbsDifferences(arr,n):
    minimum = sys.maxsize

    for i in range(n):
        sum =0 
        for j in range(n):
            sum += abs(arr[i]-arr[j])

        if sum < minimum:
            minimum = sum

        # or
        # minimum = min(minimum,sum)

    return minimum
        
arr = [2, 5, 4, 3]
n = len(arr)
print( "Required Sum = ", sumOfMinAbsDifferences(arr, n))