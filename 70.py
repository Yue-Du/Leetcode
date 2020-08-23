class Solution:
    def climbStairs(self, n: int) -> int:
        return self.climb_iter(n,1,2)
    def climb_iter(self, stairs, climb1, climb2):
        if stairs == 1:
            return climb1
        if stairs == 2:
            return climb2
        return self.climb_iter(stairs-1,climb1, climb2)+ self. climb_iter(stairs-2,climb1, climb2)

'''class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)'''