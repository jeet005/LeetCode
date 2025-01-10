# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        length = 0
        current = head
        while current:
            length += 1
            current = current.next

        first_k_node = head
        for i in range(k-1):
            first_k_node = first_k_node.next

        last_k_node = head
        for j in range(length - k):
            last_k_node = last_k_node.next

        first_k_node.val, last_k_node.val = last_k_node.val, first_k_node.val

        return head