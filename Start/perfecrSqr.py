from math import sqrt

num = 81
temp = num

sr = int(sqrt(num))
if sr * sr == temp:
    print("It is a perfect square")
else:   
    print("It is not a perfect square")