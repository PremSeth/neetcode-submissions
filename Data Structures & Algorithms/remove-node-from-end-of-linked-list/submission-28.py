# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def dfs(node):
            if node.next == None: 
                return (1, None)
            num, next = dfs(node.next)
            if num == n: 
                node.next = next
            return num+1, node.next
        dummy = ListNode(0, head)
        dummy.next = dfs(dummy)[1]
        return dummy.next