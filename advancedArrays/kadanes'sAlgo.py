



def fun(array,length):
    max = 0
    sum=0
    for i in range(length):
        sum = sum+array[i]
        if sum>max:
            max = sum
        if sum < 0:
            sum = 0
    return max
    
  




array = [-2, -3, 4, -1, -2, 1, 5, -3]
length = len(array)
print("Largest sum of subarray is: ",fun(array,length))