# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(node):
            if node == None: 
                return 0
            dist = 1 + dfs(node.next)
            if dist == n+1: 
                node.next = node.next.next
            return dist
        dummy = ListNode(0, head)
        dfs(dummy)
        return dummy.next