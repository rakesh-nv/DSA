


def min_jumps(arr):
    n = len(arr)
    
    # If the first element is 0 or array has only one element
    if n == 1:
        return 0
    if arr[0] == 0:
        return -1

    maxReach = arr[0]  # Farthest index we can reach
    steps = arr[0]      # Steps we can still take
    jumps = 1           # Jumps count
    
    for i in range(1, n):
        # If we reach the last index
        if i == n - 1:
            return jumps

        maxReach = max(maxReach, i + arr[i])  # Update maxReach
        steps -= 1  # Use a step
        
        # If no more steps are left
        if steps == 0:
            jumps += 1  # Increase jump count
            
            # If we can't move forward
            if i >= maxReach:
                return -1
            
            steps = maxReach - i  # Update steps for next jump

    return -1  # If end is not reachable

# Example usage
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
print(min_jumps(arr))  # Output: 3
