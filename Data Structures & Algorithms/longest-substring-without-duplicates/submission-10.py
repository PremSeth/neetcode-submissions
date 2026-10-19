class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        positions = {}
        start = 0
        length = 0 
        max_length = 0
        for i, j in enumerate(s): 
            print(positions)
            if j not in positions: 
                positions[j] = i
                length = i-start+1
                max_length = max(max_length, length)
            else: 
                idx = positions[j]
                while start <= idx:
                    positions.pop(s[start])
                    start+=1
                positions[j] = i
        return max_length
        

        
