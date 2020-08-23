class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.split()
        print(len(li[-1]))
        '''li=list(s)
        index=[i for i, x in enumerate(li) if x==" "]
        length=len(li)-index[-1]
        return length'''


new = Solution()
new.lengthOfLastWord(" a ")