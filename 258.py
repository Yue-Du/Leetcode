from functools import reduce
class Solution:
    def addDigits(self, num: int) -> int:
        num=list(str(num))
        while len(num)>1:
            num=reduce(lambda x,y:int(x)+int(y),num)
            num=list(str(num))
        sums = int(num[0])
        return sums

New = Solution()
New.addDigits(38)