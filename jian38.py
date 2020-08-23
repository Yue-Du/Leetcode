from typing import List
class Solution:
    def permutation(self, s: str) -> List[str]:
        length = len(s)

        def helper(res, cur, level, s):
            if level == length:
                return res.append(cur[:])

            for i in range(len(s)):
                if i>0 and s[i] == s[i - 1]:
                    continue
                cur += s[i]
                helper(res, cur, level + 1, s[:i] + s[i + 1:])
                cur = cur[:-1]
            return res

        return helper([], " ", 0, sorted(s))


New = Solution()
New.permutation("abc")