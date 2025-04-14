
def countFreq(arr, n):
    mp = dict()

    for i in range(n):
        if arr[i] in mp.keys():
            mp[arr[i]] +=1
        else:
            mp[arr[i]] = 1
    for x in mp:
        print(x ," ",mp[x])



arr = [10, 30, 10, 20, 10, 20, 30, 10]
n = len(arr)
countFreq(arr, n)