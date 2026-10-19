class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        idx = {}
        res = [-1]*len(nums1)
        for i, j in enumerate(nums1):
            idx[j] = i
        
        print(idx)
        for num in nums2:
            while stack and num > stack[-1]:
                top = stack.pop()
                res[ idx[top] ] = num
            if num in idx:
                stack.append(num)
        return res