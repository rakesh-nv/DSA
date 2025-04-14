

a=[1, 2, 0, 2, 1, 0, 2, 1, 0, 2, 0, 1,5]

for i in range(len(a)):
    for j in range(len(a)-1-i):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]

print(a)
print(a[0],a[len(a)-1])