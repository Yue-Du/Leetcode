from typing import List
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        res = -1
        i=0
        while i < len(strs):
            j=0
            while j < len(strs):
                if i==j:
                    j+=1
                    continue
                elif strs[i] in strs[j]:
                    break
                j+=1
            if j==len(strs):
                res = max(res, len(strs[i]))
            i+=1
        return res


New = Solution()
New.findLUSlength(["aabbcc", "aabbcc","cb","abc"])