


s ="{[]}("

c= 0 

for i in s:
    if i == "(":
        c +=1
    elif i==")":
        c-=1
if c==0:
    print("True")
else:
    print("False")

        

