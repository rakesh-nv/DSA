

a=[-1, 8, 1, 8, -1, 5, 1, -3]

d = []
s=[]

for i in a:
    if not i in d:
        d.append(i)
    else:
        s.append(i)
print(s)



