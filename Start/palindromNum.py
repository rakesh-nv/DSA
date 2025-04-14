

def isPalindrome(x):
    x = str(x)
    print(x)
    n = x[::-1]
    print(n)
    if x==n:
        return True
    else:
        return False

x= "naveen"
print(isPalindrome(x))