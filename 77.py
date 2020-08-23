from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        new = [i for i in range(1, n + 1)]

        def helper(res, temp, k, new):
            if len(temp) == k:
                return res.append(temp[:])

            for i in range(len(new)):
                temp.append(new[i])
                helper(res, temp, k, new[i + 1:])
                temp.pop()

                helper(res, temp, k, new[i + 1:])
            return res

        return helper([], [], k, new)

New = Solution()
New.combine(4,2)