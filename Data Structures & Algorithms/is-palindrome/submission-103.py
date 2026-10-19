class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = []
        for i in s: 
            if i.isalnum(): 
                cleaned.append(i.lower())
        return "".join(cleaned) == "".join(reversed(cleaned))