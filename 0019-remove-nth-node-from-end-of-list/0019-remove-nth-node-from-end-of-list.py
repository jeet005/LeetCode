# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next is None:
            return None
        dummy = ListNode(0, head)
        length = 0
        first = dummy
        while first:
            length += 1
            first = first.next
        
        length -= n
        first = dummy
        print('first1', first)
        while length > 1:
            length -= 1
            first = first.next
        print('first', first)
        first.next = first.next.next

        return dummy.next