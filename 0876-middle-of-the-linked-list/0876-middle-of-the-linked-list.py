# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        itr = head
        store = []
        while itr:
            store.append(itr.val)
            itr = itr.next
        
        mid = len(store)//2
        if type(mid) == float:
            mid = round(mid, 0)

        i = 0
        print(mid)
        while head:
            if i == mid:
                return head
            i += 1
            head = head.next