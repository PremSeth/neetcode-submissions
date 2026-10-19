class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        seen = {}
        length = 0
        for i,j in enumerate(s):
            while j in seen:
                seen.pop(s[left], 0)
                left +=1
            seen[j] = i
            length = max(length, i-left+1)
        return length