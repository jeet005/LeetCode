# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: Optional[ListNode], m: int, n: int) -> Optional[ListNode]:
        
        itr = head
        count = 0
        while itr:
            count += 1
            itr = itr.next

        current = head
        keep = 0
        skip = 0
        while current:
            if keep < m - 1:
                keep += 1
                current = current.next
            else:
                if skip < n and current.next:
                    current.next = current.next.next
                    skip += 1
                else:
                    temp = keep + skip
                    count -= temp
                    keep = 0
                    skip = 0
                    current = current.next
        
        return head

            
        return head