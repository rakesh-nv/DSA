

A=8
B=100000000

mul = A*B
gcd =1
for i in range(1,min(A,B)):
    if A%B ==0 and B%A==0:
        gcd = i

res = mul//gcd
print(res)
