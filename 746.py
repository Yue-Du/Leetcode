from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i-2] + cost[i], dp[i-1])
        return dp[-1]



New = Solution()
New.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])