from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            least_coin = i
            cur_coin = coins[0]

            for coin in coins:
                if i - coin >= 0 and dp[i - coin] != -1:
                    if dp[i - coin] <= least_coin:
                        cur_coin = coin
                        least_coin = dp[i - coin]
                    # least_coin = min(least_coin,dp[i-coin])
            if i - cur_coin >= 0 and dp[i - cur_coin] != -1:
                dp[i] = least_coin + 1
        return dp[-1]


New = Solution()
New.coinChange([2],3)