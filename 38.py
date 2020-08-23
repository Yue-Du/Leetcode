class Solution:
    def countAndSay(self, inp: int) -> str:
        if inp==1:
            return "1"
        n="1"
        for k in range(inp-1):
            Cas=self.transe(n)
            n=Cas
        return Cas
    
    def transe(self, n: str) -> str:
        i=0
        j=1
        count = 1
        res=""
        while j < len(n):
            if n[i]==n[j]:
                j=j+1
                count+=1
            else:
                res=res+str(count)+n[i]
                i=j
                j=i+1
                count = 1
        res = res + str(count) + n[i]
        return res


New = Solution()
New.countAndSay(3)



