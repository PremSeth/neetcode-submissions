class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            counts_s = Counter(s)
            counts_t = Counter(t)
            return counts_s == counts_t
        return False