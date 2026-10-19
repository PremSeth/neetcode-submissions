# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            left_dist = 0
            right_dist = 0
            if node.left: 
                left_dist = dfs(node.left)
            if node.right: 
                right_dist = dfs(node.right)
            if node.left == None and node.right == None: 
                return 1
            return 1 + max(left_dist, right_dist)
        if not root: 
                return 0
        return dfs(root)