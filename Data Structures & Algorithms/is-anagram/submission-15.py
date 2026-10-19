class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        if not len(s) == len(t): 
            return False
        for i,j in zip(s, t): 
            s_dict[i] = s_dict.setdefault(i, 0) + 1
            t_dict[j] = t_dict.setdefault(j, 0) + 1
        if s_dict == t_dict: 
            return True
        else: 
            return False