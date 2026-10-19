# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def rev(node, next):
            nxt = node.next
            node.next = next
            if nxt == None: 
                head = node
                return head
            return rev(nxt, node)
        if head: 
            return rev(head, None)
        return head