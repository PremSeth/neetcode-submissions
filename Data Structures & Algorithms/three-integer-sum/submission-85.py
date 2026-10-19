class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        solutions = defaultdict()
        nums.sort()
        for i in range(len(nums)): 
            left = 0
            right = len(nums)-1
            while left < right:     
                if left == i: 
                    left +=1
                if right == i: 
                    right -=1
                if left < right: 
                    total = nums[left] + nums[right] + nums[i]
                    if total < 0: 
                        left +=1
                    elif total >0: 
                        right -=1
                    else: 
                        order = [nums[left], nums[right], nums[i]]
                        order.sort()
                        solutions[tuple(order)] =1
                        left +=1
                        right -=1
        return list(solutions.keys())