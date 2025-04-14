

# arr = [10, 20, 30, 40, 40, 50, 50, 50]

# mp = dict()

# for i in range(len(arr)):
#     if arr[i] in mp.keys():
#         mp[arr[i]]+=1
#     else:
#         mp[arr[i]]=1


# sorted_keys = sorted(mp.keys())

# for i in range(len(sorted_keys)-1):
#     for j in range(len(sorted_keys)-1-i):
#         if mp[sorted_keys[j]]<mp[sorted_keys[j+1]]:
#             temp=sorted_keys[j]
#             sorted_keys[j]=  sorted_keys[j+1]
#             sorted_keys[j+1]=temp
        
# sorted_mp = {key: mp[key] for key in sorted_keys}


# for i in sorted_mp:
#     print(i,end=" ")

arr = [10, 30, 10, 20, 10, 20, 30, 10,30]
new_lst=[] #10 
count1=[] #4 

for i in range(len(arr)):
    if arr[i] not in new_lst:
        a=arr.count(arr[i])
        count1.append(a)
        new_lst.append(arr[i]) 
# print(arr[i],a,end=" ")

for i in range(len(new_lst)):
    for j in range(count1[i]):
        print(new_lst[i],end=" ")  