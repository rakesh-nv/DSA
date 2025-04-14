


a=[ 7, 5, -2, 1, -3 ]
p=0
for i in range(len(a)):
    if a[i]<0:
        a[i],a[p]=a[p],a[i]
        p +=2
print(a)