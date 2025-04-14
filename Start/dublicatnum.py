

a = "kjlsdkjfldf"

b={}

for i in a:
    if not i in b:
        b[i]=1
    else:
        b[i]=b[i]+1

for i in b:
    print(i,b[i])

