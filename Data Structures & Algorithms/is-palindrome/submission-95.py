class Solution:
    def isPalindrome(self, s: str) -> bool:
        table = str.maketrans({" ": "", "?": '', '!': '', '.': '', "'": '', ',': '', ':': ''})
        cleaned = s.translate(table).lower()
        print(cleaned)
        return cleaned == "".join(reversed(cleaned))