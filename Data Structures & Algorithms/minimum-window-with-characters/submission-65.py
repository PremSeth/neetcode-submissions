class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_letters = defaultdict(int)
        s_count = defaultdict(int)
        s_lookup = defaultdict(deque)
        for i in t: 
            t_letters[i] +=1
        left = 0
        right = 0
        shortest = ""
        count = 0
        valid = False
        best_idx = [0, 0]
        while right < len(s): 
            s_lookup[s[right]].append(right)
            s_count[s[right]] +=1
            if all(t_letters[key] <= s_count[key] for key in t_letters):
                valid = True
            else: 
                valid = False
            while valid: 
                if count > 0: 
                    if right-left < best_idx[1]-best_idx[0]: 
                        best_idx[0] = left
                        best_idx[1] = right+1
                else: 
                    best_idx[0] = left
                    best_idx[1] = right+1
                    count +=1
                s_count[s[left]] -=1
                if s_count[s[left]] ==0: 
                    s_count.pop(s[left])
                s_lookup[s[left]].popleft()
                if s[left] in t_letters: 
                    if t_letters[s[left]] <= s_count[s[left]]:
                        valid = True
                    else: 
                        valid = False
                left+=1
            right +=1
        return s[best_idx[0]:best_idx[1]]

