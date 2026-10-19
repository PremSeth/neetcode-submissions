# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def flip(node):
            if node: 
                left = node.left
                right = node.right
                node.left = flip(right)
                node.right = flip(left)
                return node
            else: 
                return None
        flip(root)
        return root


        