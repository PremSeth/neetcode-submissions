class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = defaultdict(int)
        s2_freq = defaultdict(int)
        if len(s2) < len(s1):
            return False
        for i in s1: 
            s1_freq[i] +=1
        for i in range(len(s1)):
            s2_freq[s2[i]] +=1
        if s1_freq == s2_freq: 
            return True
        left = 0
        right = len(s1)-1
        while right < len(s2)-1:
            s2_freq[s2[left]] -=1
            if s2_freq[s2[left]] == 0: 
                s2_freq.pop(s2[left])
            left+=1
            right+=1
            s2_freq[s2[right]]+=1
            print(s1_freq, s2_freq)
            if s1_freq == s2_freq:
                return True
        return False
