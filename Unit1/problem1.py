# You are organizing a prestigious event, and you must arrange the order in which guests 
# arrive based on a set of instructions.

# The instructions are provided as a 0-indexed string arrival_pattern of length n, 
# consisting of the characters:
# 'I' - The next guest should have a higher number than the previous guest.
# 'D' - The next guest should have a lower number than the previous guest.
# You need to create a string guest_order of length n + 1 that satisfies the following conditions:

# guest_order contains each number from 1 to str(n + 1) exactly once. These numbers 
# represent the guests' assigned numbers.
# For every index i from 0 to n - 1:
# If arrival_pattern[i] == 'I', then guest_order[i] < guest_order[i + 1].
# If arrival_pattern[i] == 'D', then guest_order[i] > guest_order[i + 1].
# Among all valid orders, return the lexicographically smallest one.

def arrange_guest_arrival_order(arrival_pattern):
    n = len(arrival_pattern)
    result = []
    stack = []

    for i in range (n+1):
       stack.append(i+1) #push guest number 1-indexed

       if i == n or arrival_pattern[i] =='I':
        while stack:
       
           result.append(stack.pop())
    return ''.join(map(str, result))

print(arrange_guest_arrival_order("IIIDIDDD"))  


# Time & Space Complexity: O(n) for both — each element is pushed and popped exactly once.
