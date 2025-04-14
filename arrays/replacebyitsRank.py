
def changeArr(arr):
    uneq_arr = []
    
    
    for i in arr:
        if not i in uneq_arr:
            uneq_arr.append(i)
    sortedarr = sorted(uneq_arr)
    

   

    for i in range(len(uneq_arr)):
        for j in range(len(sortedarr)):
            if uneq_arr[i] == sortedarr[j]:
                print(j+1,end=" ")

# Driver Code
arr = [100, 2, 70, 12 , 90]
changeArr(arr)


