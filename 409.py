class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt={}
        new=set(s)
        sum=0
        for i in new:
            cnt[i]=list(s).count(i)
        for i in new:
            if cnt[i]%2==0:
                sum=sum+cnt[i]
            else:
                sum=sum+cnt[i]-1
        if sum < len(s):
            sum=sum+1
        return sum


New = Solution()
New.longestPalindrome("abccccdd")