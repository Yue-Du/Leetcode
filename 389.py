from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = set(s)
        s2 = set(t)
        s2_cnt={}
        s1_cnt={}
        output=""
        for i in s2:
            s2_cnt[i]=t.count(i)
        for i in s1:
            s1_cnt[i]=s.count(i)
        '''differ = s2_cnt.keys() ^ s1_cnt.keys()'''
        for k in s2_cnt.keys():
            if k not in s1_cnt.keys():
                output = output+k
            else:
                n = s2_cnt[k]-s1_cnt[k]
                i=1
                while i <=n:
                    output = output+k
                    i=i+1
        print(output)


New = Solution()
New.findTheDifference("a", "aa")