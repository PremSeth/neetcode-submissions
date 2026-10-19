# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            last = ListNode(val =head.val, next=None)
            curr = head.next
            while curr: 
                rev = ListNode(val=curr.val, next=last)
                curr = curr.next
                last = rev
            return last
        else:
            return None