# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes =[]
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        return nodes[math.ceil((len(nodes)-1)/2)] 