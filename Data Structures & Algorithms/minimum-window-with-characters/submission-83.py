class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = {}
        s_letters = {}
        need = 0
        for i in t: 
            t_letters[i] = t_letters.get(i, 0) +1
        need = len(t_letters)

        left = 0
        right = 0
        have = 0
        solution = [0, math.inf]
        while right < len(s): 
            s_letters[s[right]] = s_letters.get(s[right], 0) +1 
            if s[right] in t_letters and s_letters[s[right]] == t_letters[s[right]]: 
                have +=1
            while have == need:
                if (right+1-left < solution[1]-solution[0]):
                    solution[0] = left
                    solution[1] = right+1
                s_letters[s[left]] -=1
                if s[left] in t_letters: 
                    if s_letters[s[left]] < t_letters[s[left]]:
                        have -=1
                left +=1
            right +=1
        if solution[1] == math.inf: 
            return ""
        return s[solution[0]:solution[1]]
