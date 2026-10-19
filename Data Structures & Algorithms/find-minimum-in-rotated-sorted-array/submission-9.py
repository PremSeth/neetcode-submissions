class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)
        curr = -1*math.inf
        first_idx = (left+right)//2
        if len(nums) == 1: 
            return nums[0]
        while left <= right:
            mid = (left+right)//2
            if mid >= len(nums):
                left = 0
                right = first_idx-1
                continue
            if mid == 0: 
                left_check = -1
                right_check = 1
            elif mid == len(nums)-1: 
                left_check = len(nums)-2
                right_check = 0
            else: 
                left_check = mid-1
                right_check = mid+1
            if nums[mid] > nums[left_check] and nums[mid] > nums[right_check]:
                return nums[right_check]
            elif nums[mid] > nums[left_check] and nums[mid] < nums[right_check]:
                left = mid+1
            else: 
                right = mid-1                
