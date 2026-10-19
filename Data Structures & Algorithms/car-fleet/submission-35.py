class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vals = {}
        for i,j in zip(position, speed):
            vals[i] = j
        vals = sorted(vals.items())
        times = []
        for i in vals:
            times.append((target-i[0])/i[1])
        fleets = [times[-1]]
        for i in reversed(times): 
            print(fleets)
            if i > fleets[-1]:
                fleets.append(i)
            else: 
                pass
        return len(fleets)