class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        last = intervals[0]
        sol = [last]
        for i in range(1, len(intervals)): 
            curr = intervals[i]
            if curr[0] <= sol[-1][-1]: 
                sol[-1][-1] = max(sol[-1][-1], curr[-1])
            else: 
                sol.append(curr)
        return sol