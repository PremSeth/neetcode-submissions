class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(int)
        curr = -1*math.inf
        for i in range(k): 
            window[nums[i]] +=1
            if nums[i] > curr: 
                curr = nums[i]
        left = 0
        maxes = []
        maxes.append(curr)
        print(window, nums[left])
        for right in range(k, len(nums)):
            window[nums[left]] -=1
            if window[nums[left]] == 0: 
                window.pop(nums[left])
            left+=1
            window[nums[right]] +=1
            maxes.append(max(window))
        return maxes