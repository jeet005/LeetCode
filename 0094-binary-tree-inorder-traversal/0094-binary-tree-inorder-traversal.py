# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = self.helper(root)
        return res

    def helper(self, root):
        elements = []
        if root is not None:
            if root.left:
                elements += self.helper(root.left)
            
            elements.append(root.val)

            if root.right:
                elements += self.helper(root.right)

        return elements
            