# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        idx = 0
        for i in lists: 
            if i: 
                heapq.heappush(heap, (i.val, idx, i))
                idx +=1
        dummy = ListNode(0)
        curr = dummy
        while heap: 
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
            if curr.next: 
                heapq.heappush(heap, (curr.next.val, idx, curr.next))
                idx +=1
        return dummy.next


        