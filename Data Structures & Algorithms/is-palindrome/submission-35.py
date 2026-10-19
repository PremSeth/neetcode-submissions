class Solution:
    def isPalindrome(self, s: str) -> bool:
        import string
        cleaned = []
        for i in s:
            if not i == " " and not i in string.punctuation:
                cleaned.append(i.lower())
        print(cleaned)
        return "".join(cleaned) == "".join(reversed(cleaned))    