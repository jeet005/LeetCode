# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        temp = ListNode(0)
        temp1 = temp
        while list1 and list2:
            if list1.val <= list2.val:
                temp1.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                temp1.next = ListNode(list2.val, None)
                list2 = list2.next
            temp1 = temp1.next

        temp1.next = list1 if list1 is not None else list2

        return temp.next