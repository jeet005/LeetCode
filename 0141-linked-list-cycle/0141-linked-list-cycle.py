# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return False

        tmp = head.next
        hmap = set()
        
        while tmp:
            if tmp in hmap:
                return True
            else:
                hmap.add(tmp)
                tmp = tmp.next
            
        return False
        