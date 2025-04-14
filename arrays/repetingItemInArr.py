
arr = [10, 30, 40, 20, 10, 20, 50, 10]

mp = dict()

for i in arr:
    if i in mp:
        mp[i] +=1
    else:
        mp[i]=1

# Remove Duplicate Elements
for i in mp:
    print(i,end=" ")
print(" ")


# repeting Elements
print("Repeting elements")
for i in mp:
    if mp[i] > 1:
        print(i,end=" ")

print("")
print("non Repeting elements")

# non repeting Elements
for i in mp:
    if mp[i] <= 1:
        print(i,end=" ")

