# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): 
            if not node: 
                return 0, True
            hL, balance_left = dfs(node.left)
            if not balance_left: 
                return 0, False
            hr, balance_right = dfs(node.right)
            if not balance_right: 
                return 0, False
            return max(1+hL, 1+hr), abs(hL-hr) <=1

        height, balanced = dfs(root) 
        return balanced