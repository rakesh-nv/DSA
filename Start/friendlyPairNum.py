



def printDivisors(n,factors):
    sum =0
    for i in range(1,n//2+1):
        if n% i ==0:
            sum = sum+i

    return sum

a1=6
a2=28
sum1 = printDivisors(a1,[])
sum2 = printDivisors(a2,[])

if sum1//a1 == sum2//a2:
    print(a1,a2,"They are friendly pair numbers")
else:
    print(a1,a2,"They are not friendly pair numbers")



