from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        i=0
        j=0
        res=0
        g=sorted(g)
        s=sorted(s)
        while j < len(s):
            if s[j]>=g[i]:
                res=res+1
                i=i+1
                j=j+1
                if i >= len(g):
                    return res
            else:
                j=j+1
        return res

New = Solution()
New.findContentChildren([1,2,3],[1,1])