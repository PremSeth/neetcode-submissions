class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_freq = defaultdict(int)
        for i in t: 
            t_freq[i] +=1
        s_freq = defaultdict(int)
        left = 0
        count = 0
        conditions = len(t_freq)
        shortest_length = math.inf
        length = 0
        best = []
        for right in range(len(s)):
            if s[right] in t_freq:
                s_freq[s[right]]+=1
                if s_freq[s[right]] == t_freq[s[right]]: 
                    count+=1 
            while count == conditions: 
                length = right-left
                if length < shortest_length: 
                    best.append(s[left:right+1])
                    shortest_length = length
                if s[left] in t_freq: 
                    s_freq[s[left]]-=1
                    if s_freq[s[left]] < t_freq[s[left]]:
                        count-=1
                left+=1
        if best: 
            return best[-1]
        return ""
            
        