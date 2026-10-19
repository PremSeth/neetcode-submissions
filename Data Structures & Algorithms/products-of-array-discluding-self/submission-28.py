class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        for i in range(len(nums)-1):
            prefix.append(nums[i] * prefix[-1])
        for i in reversed(nums[1:]): 
            suffix.append(i * suffix[-1])
        print(prefix, suffix)
        prod = []
        for i in range(len(nums)):
            prod.append(prefix[i] * suffix[len(nums)-1-i])
        return prod
