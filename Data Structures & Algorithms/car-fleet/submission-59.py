class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vals = {}
        for i,j in zip(position, speed): 
            vals[i] = j
        vals = dict(sorted(vals.items()))
        times = []
        print(vals)
        for i,j in vals.items(): 
            times.append((target-i)/j)
        print(times)
        stack = [times[-1]]
        times.reverse()
        for i in (times)[1:]:
            if i > stack[-1]:
                stack.append(i)
        return len(stack)