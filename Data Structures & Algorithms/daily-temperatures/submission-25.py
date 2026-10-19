class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            print(stack)
            if stack:
                while temp > stack[-1][1]:
                    result[stack[-1][0]] = idx-stack[-1][0]
                    stack.pop(-1)
                    if not stack:
                        break
                stack.append([idx, temp])
            else:
                stack.append([idx, temp])
        return result