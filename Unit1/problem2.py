# You are planning a special event where each attendee has a 
# unique registration number. These numbers are listed in the provided array attendees, 
# but they are currently out of order.

# At the event, attendees will walk on stage one by one following this special reveal process:

# The person at the front of the line walks on stage (this number is revealed).
# If there are still people left in line, the next person in front moves to the back of the line.
# Steps 1 and 2 repeat until everyone has walked on stage.
# Your task is to rearrange the attendees list before the process starts so that the 
# attendees walk on stage by registration number in increasing order.

# Write a function reveal_attendee_list_in_order(attendees) that returns an array 
# with the correct starting order, such that when the attendees
#  follow the above reveal process they walk on stage from smallest 
# registration number to largest registration number.

from collections import deque
def reveal_attendee_list_in_order(attendees):
    attendees =  sorted(attendees)
    dq = deque()
    #insert from the largest to the smallest

    for num in reversed(attendees):
        if dq:
            #opposite of move front to back is move back to front
            dq.appendleft(dq.pop())
        dq.appendleft(num)
    return list(dq)

    
print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 

# Time Complexity
# O(n log n)
# Because Sorting the attendees costs O(n log n)
# The reverse simulation loop is O(n)
# Total = O(n log n)
# This is optimal because you must sort the numbers.

# Space Complexity
# O(n)
# Because We store the deque of size n
# We return a list of size n
# You cannot do better since you must output n items.