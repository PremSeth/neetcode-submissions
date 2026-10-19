# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val == p.val or root.val == q.val: 
            return root
        def dfs(node):
            if node: 
                left = dfs(node.left)
                right = dfs(node.right)
                if left is TreeNode():
                    return left
                if right is TreeNode():
                    return right
                if node.val == p.val or node.val == q.val: 
                    if left or right: 
                        return node
                    return True
                if left and right: 
                    return node
                return left or right
            return False
        return dfs(root)