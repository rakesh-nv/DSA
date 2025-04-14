def is_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in brackets.values():
            stack.append(char)
        elif char in brackets.keys():
            if print(stack.pop(),end=" ") !=print(brackets[char]):
                return False
    
    return len(stack) == 0  # True if all are matched

# Test cases
expressions = ["(){[](}"]
for exp in expressions:
    print(f"{exp}: {'Balanced' if is_balanced(exp) else 'Not Balanced'}")
