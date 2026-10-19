class Solution:
    def climbStairs(self, n: int) -> int:
        temp = 0
        n1 = 1
        n2 = 2
        if n < 3: 
            return n
        for i in range(3, n+1):
            temp = n1+n2
            n1 = n2
            n2 = temp
        return temp

         
        