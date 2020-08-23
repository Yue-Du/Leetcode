from typing import List
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vows = ["a","e","o","u","i"]
        cur = 0
        i = 0
        j = k
        for vow in s[:k]:
            if vow in vows:
                cur += 1
        res = cur
        while j < len(s):
            if s[j] in vows:
                cur += 1
            if s[i] in vows:
                cur -= 1
            i += 1
            j += 1
            res = max(res, cur)
        return res


New = Solution()
New.maxVowels("novowels",1)