

# a=[1,2,3,4,5]
# b=[4,5,6,7,8]

# intersection = []
# unian=a

# for i in b:
#     if i not in a:
#         unian.append(i)
#     if i in a:
#         intersection.append(i)

# print(intersection)
# print(unian)


a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8]


intersection = [i for i in b if i in a]  # Finding common elements
union = list(set(a + b))  # Combining both lists and removing duplicates

print("Intersection:", intersection)
print("Union:", union)
