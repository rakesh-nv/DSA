
# def leftRotate(arr,d,n):
#     for i in range(d):
#         temp = arr[0]
#         for j in range(n-1):
#             arr[j]=arr[j+1]
#         arr[n-1]=temp
#     print(arr)    

def rightRotate(arr,d,n):
    for i in range(d):
        temp = arr[n-1]   
        for j in range(n-1,0,-1):
            arr[j]=arr[j-1]
        arr[0]=temp
    print(arr) 
            
# left rotate
arr = [10, 20, 30, 40, 50, 60, 70]
# leftRotate(arr, 3, 7)
rightRotate(arr,2,7)


