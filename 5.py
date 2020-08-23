class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        n=len(s)
        i=0
        max_len=1
        res=s[0]
        while i < n:
            j=i
            k=i
            while j-1>=0  and k+1<n and s[j-1]==s[k+1]:
                j=j-1
                k=k+1
            if k-j+1 > max_len:
                res=s[j:k+1]
                max_len=k-j+1
            i=i+1
        h=0
        while h < n-1:
            p1=h
            p2=h+1
            while p1>=0 and p2<n and s[p1]==s[p2]:
                if p2-p1+1 > max_len:
                    res=s[p1:p2+1]
                    max_len=p2-p1+1
                p1=p1-1
                p2=p2+1
            h=h+1
        return res


New = Solution()
New.longestPalindrome("babad")