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
            j = i
            while j: 
                heapq.heappush( heap, (j.val, idx, j) )
                idx +=1
                j = j.next
        dummy = ListNode(0)
        curr = dummy
        while heap: 
            curr.next = heapq.heappop(heap)[2]
            curr = curr.next
        return dummy.next


        