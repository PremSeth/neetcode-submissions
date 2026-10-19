class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i,j in enumerate(temperatures): 
            while stack and stack[-1][-1] < j:
                idx, temp = stack.pop()
                res[idx] = i-idx
            stack.append( (i, j))
        return res