class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cheap = 0
        st1=cost[0]
        st2 = cost[1]
        for i in cost[2:]:
            temp = min(st1+i, st2+i)
            st1 = st2
            st2=temp
        return min(st1, st2)