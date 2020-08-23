from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hashset={}
        i=0
        while i + 9 <=len(s):
            index=s[i:i+10]
            if s[i:i+10] not in hashset:
                hashset[index]=1
            else:
                hashset[index]+=1
            i=i+1
        res=[]
        for keys in hashset:
            if hashset[keys]>1:
                res.append(keys)
        return res



New = Solution()
New.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")