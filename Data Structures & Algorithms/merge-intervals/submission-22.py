class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stack = []
        intervals.sort()
        for i in intervals:
            stack.append(i)
            if len(stack) >= 2 and stack[-1][0] <= stack[-2][1]:
                start2, end2 = stack.pop()
                stack[-1][-1] = max(end2, stack[-1][-1])
        return stack