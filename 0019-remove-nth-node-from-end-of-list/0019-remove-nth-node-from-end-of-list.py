# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        current = head
        length = 0
        while current:
            length += 1
            current = current.next
        
        remove_idx = length - n
        
        if remove_idx == 0 and length <= 1:
            return None

        itr = ListNode(0)
        itr.next = head
        first = itr
        idx = 0
        while remove_idx > 0:
            remove_idx -= 1
            first = first.next
        first.next = first.next.next

        return itr.next