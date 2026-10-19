class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]*len(nums)
        suff = [1]*len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
        for i in reversed(range(0, len(nums)-1)):
            suff[i] = suff[i+1]*nums[i+1]
        output = [] 
        for i in range(0, len(nums)):
            output.append(pre[i]*suff[i])
        return output

