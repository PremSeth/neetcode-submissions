class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        
        indexes = {(temp, idx): idx for idx, temp in enumerate(temperatures)}
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                lesser = stack.pop()
                result[indexes[lesser]] = idx - indexes[lesser]
            stack.append((temp, idx))
        
        return result