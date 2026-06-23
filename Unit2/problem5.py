# LeetCode 206 — Reverse Linked List
# You’re given the head of a singly linked list, and you 
# must reverse it in-place.
# Input:  1 → 2 → 3 → 4 → 5
# Output: 5 → 4 → 3 → 2 → 1

class TreeNode:
    def __init__(self, value = 0,next = None ):
         self.value = value
         self.next = next
        
         

def buildListNode(arr):
     dummy = TreeNode() # a dummy starter node
     current = dummy
     for x in arr:
          current.next = TreeNode(x)
          current = current.next # moves forward
     return dummy.next #returns the real head

def toList(head):
     result = []
     while head:
          result.append(head.value)
          head = head.next
     return result

     

class Solution:
     def reversedLinkedList(self, head:TreeNode) -> TreeNode:
          if not head:
               return None
          prev, current = None, head

          while current:
               next = current.next
               current.next = prev
               prev = current
               current = next
          return prev
     
# T: O(n)  M: O(1)

class RecursiveSolution:
     def reversedLinkedList(self, head: TreeNode) -> TreeNode:
        #Empty List or Single Node
        if not head or not head.next:
            return head
        
        newHead = self.reversedLinkedList(head.next)

        #Flip the pointer
        head.next.next = head
        head.next = None
        return newHead
     
# T: O(n)  M: O(n)
     

array = [1,2,3,4,5,6]
headList = buildListNode(array)
recursiveHead = buildListNode(array)

solution = Solution().reversedLinkedList(headList)
solution2 = RecursiveSolution().reversedLinkedList(recursiveHead)

print(toList(solution))
print(toList(solution2))


        
