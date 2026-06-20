# You are organizing a series of events, and each event is
# represented by a parenthesis in the string schedule, where 
# an opening parenthesis ( represents the start of an event, 
# and a closing parenthesis ) represents the end of an event.
# A balanced schedule means every event that starts has a corresponding end.

# However, due to some scheduling issues, the current schedule might not be balanced. 
# In one move, you can insert either a start or an end at any position in the schedule.

# Return the minimum number of moves required to make the schedule balanced.

def min_changes_to_make_balanced(schedule):
    closing_needed = 0
    opening_needed = 0

   

    for s in schedule:
        if s == ')':
            if closing_needed > 0:
                closing_needed -= 1
            else:
                opening_needed += 1
        else:
            closing_needed += 1
      

    return opening_needed + closing_needed
  

print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("((("))

# Time complexity: O(n) — single pass

# Space: O(1) — constant extra space