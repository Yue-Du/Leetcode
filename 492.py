from typing import List
class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        l=area
        dis=area
        while l <=area:
            if area%l==0:
                w=area//l
                if l>=w and l-w<dis:
                    dis=l-w
                    temp=[l,w]
                if l<w:
                    return temp
            l-=1
        return temp


New = Solution()
New.constructRectangle(1)