# You are organizing an event, and you have a 0-indexed list guests of even length,
# where each element represents either an attendee (positive integers) or an absence
# (negative integers). The list contains an equal number of attendees and absences.

# You should return the guests list rearranged to satisfy the following conditions:

# Every consecutive pair of elements must have opposite signs, indicating that each
# attendee is followed by an absence or vice versa.
# For all elements with the same sign, the order in which they appear in the original 
# list must be preserved.
# The rearranged list must begin with an attendee (positive integer).
# Return the rearranged list after organizing the guests according to the conditions.

def rearrange_guests(guests):
    
    positive = []
    negative = []

    for g in guests:
        if g>0:
            positive.append(g)
        else:
            negative.append(g)
    result = []
    
    for p, n in zip(positive, negative):
        result.append(p)
        result.append(n)

    return result
    
print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 

# Time Complexity: O(n)
# One pass to split positives and negatives
# One pass to interleave
# Space Complexity: O(n)
