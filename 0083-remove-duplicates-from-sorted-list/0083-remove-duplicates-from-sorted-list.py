# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head
        while tmp and tmp.next:
            if tmp.next.val == tmp.val:
                tmp.next = tmp.next.next
                continue
            tmp = tmp.next
        
        return head
        