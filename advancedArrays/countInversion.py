
A = [6, 3, 5, 2, 7]

count =0
for i in range(len(A)):
    for j in range(i+1,len(A)):
        if A[i]>A[j]:
            A[i],A[j] = A[j],A[i]
            count+=1
print(A)
print(count)
