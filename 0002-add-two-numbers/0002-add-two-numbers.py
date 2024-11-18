# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = []
        list2 = []

        while l1:
            list1.append(l1.val)
            l1 = l1.next
        
        while l2:
            list2.append(l2.val)
            l2 = l2.next

        

        list1 = int(''.join(map(str, list1[::-1])))
        list2 = int(''.join(map(str, list2[::-1])))

        res = list1 + list2
        res = reversed_list = [int(digit) for digit in str(res)]
        node = None
        for x in res:
            if node:
                node = ListNode(x, node)
            else:
                node = ListNode(x, None)
            
        return node
        
        

