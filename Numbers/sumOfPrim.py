
res =0
for i in range(50,101):
    if i<2 :
        continue
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
        res +=i
print(res)

#1,2,3,4,5,6,7,8,9,10