# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        nest = []
        q = deque()
        q.append(root)
        level_size = 1
        curr = []
        while q: 
            for i in range(level_size): 
                node = q.popleft()
                if node: 
                    curr.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            level_size = len(q)
            if curr: 
                nest.append(curr)
            curr = []
        return nest
        