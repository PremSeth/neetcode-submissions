# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        if curr1 and not curr2: 
            return curr1
        if curr2 and not curr1: 
            return curr2
        if not curr1 and not curr2: 
            return None
        if curr1.val < curr2.val: 
            head = curr1
            curr1 = curr1.next
        else: 
            head = curr2
            curr2 = curr2.next
        c3 = head
        while c3: 
            if curr1 and curr2: 
                if curr1.val < curr2.val: 
                    c3.next = curr1
                    curr1 = curr1.next
                    c3 = c3.next
                else: 
                    c3.next = curr2
                    curr2 = curr2.next
                    c3 = c3.next
            if curr1 and not curr2: 
                c3.next = curr1
                curr1 = curr1.next
                c3 = c3.next
            if curr2 and not curr1: 
                c3.next = curr2
                curr2 = curr2.next
                c3 = c3.next
            if not curr1 and not curr2: 
                c3.next = None
                c3 = c3.next
        return head
