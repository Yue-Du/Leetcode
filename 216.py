from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        num = [1,2,3,4,5,6,7,8,9]
        def helper(res, cur, i, k, n_left, index):
            if index >= 9:
                return res
            elif i==k and n_left == 0:
                res.append(cur[:])
                return res
            elif i==k:
                return res

            cur.append(num[index])
            helper(res, cur, i+1, k, n_left-num[index], index+1)
            cur.pop()

            helper(res, cur, i, k, n_left, index+1)

            return res

        return helper([], [], 0, k, n, 0)


New = Solution()
New.combinationSum3(3,15)