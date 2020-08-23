from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        sort_coins=sorted(coins, reverse=True)
        count=0
        left=amount
        if amount==0:
            return 0
        while left>0:
            for i in sort_coins:
                if left<i:
                    continue
                else:
                    count+=left//i
                    left=left%i
            if left==0:
                return count
            else:
                return -1


New = Solution()
New.coinChange([186,419,83,408],6249)