from typing import List
class Solution:
    def hasAllCodes(self, k: int) -> List[int]:
        def helper(res, cur, i):
            if i == k+1:
                return res.append(cur[:])

            cur = cur + "1"
            helper(res, cur, i+1)
            cur = cur[:-1]

            cur = cur + "0"
            helper(res, cur, i+1)
            cur = cur[:-1]

            return res

        return helper([], "", 1)

New = Solution()
New.hasAllCodes(3)