


def isPasindrome(n):
  temp = n
  reversed = 0

  while n > 0:
    rem = n%10
    reversed = (reversed * 10) + rem
    n = n//10

  return temp == reversed
    

# n = 121
# isPasindrome(n)
    
def largestpalindrome(arr,n):
  currentMax = -1

  for i in range(n):
    if arr[i]>currentMax and isPasindrome(arr[i]):
      currentMax = arr[i]
  return currentMax


arr = [1,232,5545455,909090,161]
n = len(arr)

print(largestpalindrome(arr,n))
