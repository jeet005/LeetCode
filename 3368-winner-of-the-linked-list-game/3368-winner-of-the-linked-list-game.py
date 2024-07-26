# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        
        itr = head
        even_points = 0
        odd_points = 0
        # Traverse through the linked list assigning points
        while itr is not None:
            odd = itr.next
            if itr.val > odd.val:
                even_points += 1
            else:
                odd_points += 1
            itr = odd.next
            
        # Return the winning team
        if odd_points > even_points:
            return "Odd"
        elif odd_points < even_points:
            return "Even"
        else:
            return "Tie"

        