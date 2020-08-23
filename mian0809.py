from typing import List
import copy
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n, l, r, res, temp):
            if l==n and r==n:
                dcopy = copy.deepcopy(temp)
                return res.append(dcopy)
            if l < n:
                temp += '('
                helper(n, l+1, r, res, temp)
                temp = temp[:-1]
            if r < l:
                temp += ')'
                helper(n, l, r+1, res, temp)
                temp = temp[:-1]
            return res

        return helper(n, 0, 0, [], '')


New = Solution()
New.generateParenthesis(3)