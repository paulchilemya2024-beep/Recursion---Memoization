# You are organizing a large event, and you need to mark the timeline for a series 
# of scheduled activities.

# You are given two strings:

# event: A short string representing an event name.
# timeline: A longer string representing the full timeline for the event.
# Initially, the timeline is empty and represented by a string t of the same length as timeline,
# where every character is '?'.

# In one turn, you can "mark" the timeline by placing the event string over any valid position 
# in t and copying its letters onto t. This replaces the corresponding '?' characters in t.

# Rules:

# You can only place event where it fully fits within t.
# Each time you mark the timeline, the corresponding letters in t are updated.
# Your goal is to perform a sequence of marks so that t becomes exactly equal to timeline.
# You may use at most 10 * len(timeline) marks.
# Return a list of the starting indices where you placed the event string during each mark.
# If it is impossible to turn t into timeline following these rules, return an empty list.

def mark_event_timeline(event, timeline):
    # Greedy stamping algorithm (reduce timeline to all '?')
    n = len(timeline)
    m = len(event)
    if m > n:
        return []

    target = list(timeline)
    done = [False] * (n - m + 1)
    result = []

    def can_stamp(pos):
        made_change = False
        for k in range(m):
            if target[pos + k] != '?' and target[pos + k] != event[k]:
                return False
            if target[pos + k] == event[k]:
                made_change = True
        return made_change

    while True:
        progress = False
        for i in range(n - m + 1):
            if not done[i] and can_stamp(i):
                # apply stamp: replace matching characters with '?'
                changed = False
                for k in range(m):
                    if target[i + k] == event[k]:
                        target[i + k] = '?'
                        changed = True
                if changed:
                    done[i] = True
                    result.append(i)
                    progress = True
        if not progress:
            break

    if all(ch == '?' for ch in target):
        return result[::-1]
    return []

print(mark_event_timeline("abc", "ababc"))  
print(mark_event_timeline("abca", "aabcaca")) 