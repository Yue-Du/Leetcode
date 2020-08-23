'''class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cacheDict = {}
        cacheTset = set()
        for index in range(len(s)):
            cS = s[index]
            cT = t[index]
            if cS in cacheDict:
                if cacheDict[cS] == cT:
                    continue
                else:
                    return False
            else:
                if cT in cacheTset:
                    return False
                else:
                    cacheTset.add(cT)
                    cacheDict[cS] = cT
        return True'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        cachs={}
        cacht=set()
        i=0
        while i <len(s):
            if s[i] in cachs:
                if cachs[s[i]] == t[i]:
                    i=i+1
                else:
                    return False
            else:
                if t[i] in cacht:
                    return False
                else:
                    cachs[s[i]] = t[i]
                    cacht.add(t[i])
                    i=i+1


New = Solution()
New.isIsomorphic("egc","add")