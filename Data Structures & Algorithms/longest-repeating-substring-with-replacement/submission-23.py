class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0 
        freq = defaultdict(int)
        max_length = 0
        length = 0
        for right in range(len(s)):
            freq[s[right]] +=1
            length = right-left+1
            most_freq = max(freq, key = freq.get)
            while not length -freq.get(most_freq) <= k:
                freq[s[left]]-=1
                left+=1
                length = right-left+1
                most_freq = max(freq, key = freq.get)
            max_length = max(max_length, length)
        return max_length