class Solution(object):
    def waysToChange(self, n):

        num = [25, 10, 5, 1]
        cnt = [1]

        def helper(i, res, left_n):
            if left_n == 0:
                res += cnt
                return res
            elif i == 3:
                return
            elif left_n < num[i]:
                return
            for k in range((left_n // num[i]) + 1):
                left_n = left_n - k * num[i]
                helper(i + 1, res, left_n)
                left_n = left_n + k * num[i]
            return sum(res)
        return helper(0, [0], n)

New = Solution()
New.waysToChange(25)