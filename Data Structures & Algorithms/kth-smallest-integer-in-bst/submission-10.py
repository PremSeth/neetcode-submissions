# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ordered = []
        def unravel(node):
            if node == None:
                return 
            unravel(node.left)
            ordered.append(node.val)
            unravel(node.right)
        unravel(root)
        return ordered[k-1]
