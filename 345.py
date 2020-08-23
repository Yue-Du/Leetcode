class Solution:
    def reverseVowels(self, s: str) -> str:
        yy=["a","e","i","o","u"]
        left=0
        right=len(s)-1
        s=list(s)
        while left < right:
            if s[left] in yy:
                if s[right] in yy:
                    med = s[left]
                    s[left]=s[right]
                    s[right]=med
                    left = left + 1
                    right = right - 1
                else:
                    right=right-1
            else:
                left=left+1
        s = "".join(s)
        return s


New = Solution()
New.reverseVowels("leetcode")