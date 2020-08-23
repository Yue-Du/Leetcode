class Solution:
    def waysToChange(self, n: int) -> int:
        coins = [25, 10, 5, 1]

        def findCombination(money, level, res):
            if level == 3 or money < 0:
                res.append(1)
                return

            if money < coins[level]:
                findCombination(money, level + 1, res)
            for i in range(1 + (money // coins[level])):
                findCombination(money - i * coins[level], level + 1, res)
            return sum(res)

        return findCombination(n, 0, [])
New = Solution()
New.waysToChange(5)