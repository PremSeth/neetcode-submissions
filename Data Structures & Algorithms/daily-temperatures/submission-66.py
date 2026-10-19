class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lesser = stack.pop()
                result[lesser[1]] = idx - lesser[1]
            stack.append((temp, idx))
        
        return result