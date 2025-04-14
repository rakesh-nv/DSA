

String = 'GuDDuBHaiyA'

str1=str()

for i in String:
    if 65<=ord(i) and ord(i)<=90:
       str1 += chr(ord(i)+32)
    if 97<=ord(i) and ord(i)<=122:
        str1 += chr(ord(i)-32)
        
print(str1)