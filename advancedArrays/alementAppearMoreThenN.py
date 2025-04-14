

arr = [4,4,4,4,4,4,4,4,2,2,2,2,2,5,5,5,5]

n=len(arr)
k=4
num=n//k
print(num)
count = dict()
for i in range(n):
    if arr[i] in count:
        count[arr[i]]+=1
    else:
        count[arr[i]]=1
for i in count:
    if count[i]>num:
        print(i,end=" ")


